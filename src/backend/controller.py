import certificate
from logger import logger


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
def main():
    logger.warning("Logger is in diagnose mode")
    certificate_id = "1"
    start_time = 1715836780
    end_time = 1715836780
    company_name = "YourCompanyName"
    amount = float(100)

    # Create a certificate
    #    create_certificate(certificate_id, amount, start_time, end_time, company_name)
    # print(verify_certificate(certificate_id, amount))
    # print(verify_certificate(certificate_id, amount // 2))


if __name__ == "__main__":
    main()
