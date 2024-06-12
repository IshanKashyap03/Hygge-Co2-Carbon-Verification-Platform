import asyncio
from datetime import datetime
from typing import Tuple

from backend.blockchain_publisher import models
from backend.blockchain_publisher.accounting_client import (
    BlockchainCertificatePublisher,
)
from backend.common import certificate
from backend.common.logger import logger, logger_close, logger_setup


@logger.catch
def generate_certificate(
    certificate_id: str,
    amount: float,
    start_time: datetime,
    end_time: datetime,
    company_name: str,
    issue_date: datetime,
    user_id: str,
) -> Tuple[str, str, datetime] | None:
    if start_time > end_time:
        logger.warning("Start time must be less than end time")
        return
    if amount < 0:
        logger.warning("Amount can't be negative")
        return

    # Certificate ids must be unique in the database
    if models.does_certificate_exist(certificate_id):
        logger.warning(
            "Certificate with {certificate_id} already exists in the database",
            certificate_id=certificate_id,
        )
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
    transaction_date = datetime.now()
    actual_transaction_hash = transaction_hash.hex()

    models.certificate_add_transaction(
        certificate_id, actual_transaction_hash, transaction_date
    )
    certificate_address = "certificate_address"
    return actual_transaction_hash, certificate_address, transaction_date


async def main():
    logger_setup("hcevp_blockchain_publisher")
    logger.success("Blockchain publisher starting up")

    models.database_setup()
    certificate.setup_certificate_module()
    client = BlockchainCertificatePublisher(generate_certificate, logger)
    client.start()

    logger.success("Blockchain publisher started")

    try:
        # script keeps running
        while True:
            pass
    except KeyboardInterrupt:
        client.stop()

    logger.success("Blockchain publisher shutting down")
    # Close the logger, this should be the last line of the shutdown code
    await logger_close()


if __name__ == "__main__":
    asyncio.run(main())
