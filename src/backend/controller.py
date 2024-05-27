from contextlib import asynccontextmanager
import certificate
from accounting_client import CertificateDataClient
from logger import logger, logger_close


@asynccontextmanager
async def lifespan(_):
    """
    This function is called when the application starts up and shuts down. It is used to initialize and clean up resources.
    Used by FastAPI to manage the application's lifecycle.
    """
    logger.info("Application starting up")
    # Add startup code after this line but before the yield
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
    if amount < 0:
        logger.warning("Amount must be positive")
        return {"status": "warning, amount must be positive"}

    verification_hash = certificate.hash_data(certificate_id, str(amount))
    if not certificate.verify_certificate(verification_hash):
        logger.warning("Certificate not verified")
        return {"status": "Not Verified"}

    # TODO: Search database for name
    return {"status": "Verified", "companyName": "Satyam Steel"}


@logger.catch
def create_certificate(
    certificate_id: str,
    amount: float,
    start_time: int,
    end_time: int,
    company_name: str,
) -> None:
    if start_time > end_time:
        logger.warning("Start time must be less than end time")
        return
    if amount < 0:
        logger.warning("Start time must be less than end time")
        return
    verification_hash = certificate.hash_data(certificate_id, str(amount))
    computed_hash = certificate.hash_data(
        str(certificate_id), str(amount), str(start_time), str(end_time), company_name
    )
    # TODO: Add logging for the transaction
    certificate.create_certificate(computed_hash, verification_hash)


# Example usage
# TODO: Remove this or replace with actual usage
def main():
    print("Creating certificate")
    certificate_id = "cert-ca-1399"
    start_time = 1715836780
    end_time = 1715836780
    company_name = "Satyam Steel"
    amount = 171.933

    # Create a certificate
    create_certificate(certificate_id, amount, start_time, end_time, company_name)
    print(verify_certificate(certificate_id, amount))
    print(verify_certificate(certificate_id, amount // 2))


if __name__ == "__main__":
    main()
