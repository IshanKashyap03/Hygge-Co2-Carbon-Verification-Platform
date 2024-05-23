import certificate


def verify_certificate(certificate_id: str, amount: float) -> dict:
    if amount < 0:
        # TODO: Add logging
        return {"status": "Error, amount must be positive"}

    verification_hash = certificate.hash_data(certificate_id, str(amount))
    print(verification_hash)
    if not certificate.verify_certificate(verification_hash):
        return {"status": "Not Verified"}

    # TODO: Search database for name
    return {"status": "Verified", "companyName": "Satyam Steel"}


def create_certificate(
    certificate_id: str,
    amount: float,
    start_time: int,
    end_time: int,
    company_name: str,
) -> None:
    if start_time > end_time:
        # TODO: Add logging
        return
    if amount < 0:
        # TODO: Add logging
        return
    verification_hash = certificate.hash_data(certificate_id, str(amount))
    computed_hash = certificate.hash_data(
        str(certificate_id), str(amount), str(start_time), str(end_time), company_name
    )
    # TODO: Add logging for the transaction
    certificate.create_certificate(computed_hash, verification_hash)


# Example usage
def main():
    certificate_id = "1"
    start_time = 1715836780
    end_time = 1715836780
    company_name = "YourCompanyName"
    amount = float(100)

    # Create a certificate
    create_certificate(certificate_id, amount, start_time, end_time, company_name)
    print(verify_certificate(certificate_id, amount))
    print(verify_certificate(certificate_id, amount // 2))


if __name__ == "__main__":
    main()
