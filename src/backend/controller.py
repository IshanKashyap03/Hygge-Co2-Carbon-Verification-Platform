from contextlib import asynccontextmanager
import certificate
from accounting_client import CertificateDataClient
from logger import logger, logger_close
from datetime import datetime
import models
from utils import start_end_datetime_to_str


@asynccontextmanager
async def lifespan(_):
    """
    This function is called when the application starts up and shuts down. It is used to initialize and clean up resources.
    Used by FastAPI to manage the application's lifecycle.
    """
    logger.info("Application starting up")
    # Add startup code after this line but before the yield
    models.database_setup()
    client = CertificateDataClient(create_certificate, logger)
    client.start()

    yield
    logger.info("Application shutting down")
    # Add shutdown code after this line
    client.stop()

    # Close the logger, this should be the last line of the shutdown code
    await logger_close()


@logger.catch
def verify_certificate(certificate_id: str, amount: float) -> dict:
    if not models.does_certificate_exist(certificate_id):
        logger.warning("Certificate does not exist")
        return {"status": "Not Verified"}

    if amount < 0:
        logger.warning("Amount can't be negative")
        models.certificate_verification_attempt_create(certificate_id, amount, False)
        return {"status": "Warning, amount can't be negative"}

    verification_hash = certificate.hash_data(certificate_id, str(amount))
    if not certificate.verify_certificate(verification_hash):
        logger.warning("Certificate not verified")
        models.certificate_verification_attempt_create(certificate_id, amount, False)
        return {"status": "Not Verified"}

    models.certificate_verification_attempt_create(certificate_id, amount, True)
    certificate_date = models.certificate_get_data(certificate_id)
    return {
        "status": "Verified",
        "companyName": certificate_date["factory_name"],
        "startDate": start_end_datetime_to_str(certificate_date["start_date"]),
        "endDate": start_end_datetime_to_str(certificate_date["end_date"]),
    }


@logger.catch
def create_certificate(
    certificate_id: str,
    amount: float,
    start_time: datetime,
    end_time: datetime,
    company_name: str,
    issue_date: datetime,
    user_id: str,
) -> None:
    if start_time > end_time:
        logger.warning("Start time must be less than end time")
        return
    if amount < 0:
        logger.warning("Amount can't be negative")
        return
    # Create user if not present
    models.user_create(user_id)

    # Add data from certificate to the database
    models.certificate_create(
        certificate_id, amount, start_time, end_time, company_name, issue_date, user_id
    )

    # Hash the data needed for certificate
    verification_hash = certificate.hash_data(certificate_id, str(amount))
    computed_hash = certificate.hash_data(
        str(certificate_id), str(amount), str(start_time), str(end_time), company_name
    )

    models.certificate_set_transaction_status(
        certificate_id, models.TransactionStatus.IN_PROGRESS
    )

    # Attempt to create a certificate on the blockchain
    transaction = None
    try:
        transaction = certificate.create_certificate(computed_hash, verification_hash)
    except Exception as e:
        logger.error("Error creating certificate: {exception}", exception=e)
        models.certificate_set_transaction_status(
            certificate_id, models.TransactionStatus.FAILED
        )
        return

    # Unknown error
    if transaction is None:
        logger.error(
            "Error creating certificate: {transaction}", transaction=transaction
        )
        models.certificate_set_transaction_status(
            certificate_id, models.TransactionStatus.FAILED
        )
        return

    # Transaction was reverted by EVM
    if transaction["status"] != certificate.ETHEREUM_TRANSACTION_SUCCESS:
        logger.error(
            "Error creating certificate: {transaction}", transaction=transaction
        )
        models.certificate_set_transaction_status(
            certificate_id,
            models.TransactionStatus.REVERTED,
        )
        return

    # Based on the version of Python not the package it uses different attribute names
    try:
        transaction_hash = transaction["transactionHash"]
    except KeyError:
        transaction_hash = transaction["transaction_hash"]

    # Add transaction details to the database as was successful
    models.certificate_add_transaction(
        certificate_id,
        transaction_hash.hex(),
        datetime.now(),
    )
