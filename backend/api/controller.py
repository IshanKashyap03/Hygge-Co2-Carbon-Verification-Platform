from contextlib import asynccontextmanager
from datetime import datetime
from typing import Any, Callable

import backend.common.certificate as certificate
from backend.api import models
from backend.api.accounting_client import CertificateDataClient
from backend.common.logger import logger, logger_close, logger_setup
from backend.common.utils import (
    issue_date_to_datetime,
    start_end_date_to_datetime,
    start_end_datetime_to_str,
)


@asynccontextmanager
async def lifespan(_):
    """
    This function is called when the application starts up and shuts down. It is used to initialize and clean up resources.
    Used by FastAPI to manage the application's lifecycle.
    """
    logger_setup("hcevp_api")  # This must be the first line
    logger.info("Application starting up")
    certificate.setup_certificate_module()
    models.database_setup()
    client = CertificateDataClient(create_certificate, logger)
    client.start()

    yield

    logger.info("Application shutting down")
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
    transaction_hash: str,
    transaction_date: datetime,
    certificate_address: str,
) -> None:
    if models.does_certificate_exist(certificate_id):
        logger.warning(
            "Certificate {certificate_id} already exists", certificate_id=certificate_id
        )
        return

    verificatation_hash = certificate.hash_data(certificate_id, str(amount))
    if not certificate.verify_certificate(verificatation_hash):
        logger.warning("Certificate doesn't exists on the chain. ")
        return

    models.user_create(user_id)
    models.certificate_create(
        certificate_id,
        amount,
        start_time,
        end_time,
        company_name,
        issue_date,
        user_id,
        transaction_hash,
        transaction_date,
        certificate_address,
    )
    logger.info("Certificate {certificate_id} created", certificate_id=certificate_id)


def get_data_from_user(prompt: str, convert: Callable[[str], Any]) -> Any:
    while True:
        raw_data = input(prompt)
        try:
            data = convert(raw_data)
            return data
        except ValueError:
            print(f"Raw data: {raw_data} can't be converted")


def add_certificate_to_backend():
    while input("Do you want to add a certificate to the backend (y/n): ") == "y":
        # Get user data
        certificate_id = input("Enter certificate id: ")
        if models.does_certificate_exist(certificate_id):
            print(
                f"Certificate {certificate_id} already exists. Exiting",
            )
            continue
        company_name = input("Enter company name: ")
        start_date: datetime = get_data_from_user(
            "Enter start date: ", start_end_date_to_datetime
        )
        end_date: datetime = get_data_from_user(
            "Enter end date: ", start_end_date_to_datetime
        )
        total_emissions: float = get_data_from_user(
            "Enter total CO2 emissisons: ", float
        )
        issue_date: datetime = get_data_from_user(
            "Enter issue date: ", issue_date_to_datetime
        )
        user_id = input("Enter user id: ")
        transaction_hash = input("Enter transaction hash: ")

        # Verify and create
        verificatation_hash = certificate.hash_data(
            certificate_id, str(total_emissions)
        )
        if not certificate.verify_certificate(verificatation_hash):
            print("Certificate doesn't exists on the chain. You must create it")
            continue
        models.user_create(user_id)
        models.certificate_create(
            certificate_id,
            total_emissions,
            start_date,
            end_date,
            company_name,
            issue_date,
            user_id,
            transaction_hash,
            datetime.now(),
            "",
        )
        print(f"Successful added certificate {certificate_id}")


def main():
    add_certificate_to_backend()


if __name__ == "__main__":
    main()
