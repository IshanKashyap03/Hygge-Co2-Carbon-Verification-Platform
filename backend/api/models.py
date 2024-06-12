from copy import deepcopy
from datetime import datetime

import peewee as sql

from backend.common.config import (
    DATABASE_HOST,
    DATABASE_NAME,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_USER,
)

psql_db = sql.PostgresqlDatabase(
    DATABASE_NAME,
    user=DATABASE_USER,
    password=DATABASE_PASSWORD,
    host=DATABASE_HOST,
    port=DATABASE_PORT,
)


class BaseModel(sql.Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = psql_db


class User(BaseModel):
    id = sql.BigAutoField(primary_key=True)
    account_id = sql.CharField(max_length=50, unique=True, null=False)


class Certificate(BaseModel):
    id = sql.BigAutoField(primary_key=True)

    # Certificate details obtained from accounting tool:
    account_id = sql.ForeignKeyField(User, backref="certificate", field="account_id")
    certificate_number = sql.CharField(max_length=50, unique=True, null=False)
    factory_name = sql.CharField(
        max_length=255, null=False
    )  # Wouldn't the company name be linked to the account?
    start_date = sql.DateTimeField(null=False)
    end_date = sql.DateTimeField(null=False)
    total_emission = sql.DecimalField(null=False, decimal_places=4, max_digits=12)
    issue_date = sql.DateTimeField(null=False)

    created_date = sql.DateTimeField(null=False)

    # Transaction details:
    transaction_date = sql.DateTimeField(null=True)
    transaction_hash = sql.CharField(max_length=64, null=True, default=None)
    certificate_address = sql.CharField(max_length=40, null=True, default=None)


class CertificateVerificationAttempt(BaseModel):
    certificate_number = sql.ForeignKeyField(
        Certificate,
        backref="certificate_verification_attempts",
        field="certificate_number",
    )
    total_emission = sql.DecimalField(null=False, decimal_places=4, max_digits=12)
    verified_time = sql.DateTimeField(null=False)
    success = sql.BooleanField(null=False)


def does_certificate_exist(certificate_id: str) -> bool:
    return (
        Certificate.select()
        .where(Certificate.certificate_number == certificate_id)
        .exists()
    )


def user_create(account_id: str) -> bool:
    """
    Creates a new user in the database with the given account_id if they don't exist and returns true if created successfully.
    Otherwise, returns false.
    """
    if not User.select().where(User.account_id == account_id).exists():
        User.create(account_id=account_id)
        return True
    return False


def certificate_create(
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
    """Creates a new certificate in the database."""
    user = User.get(User.account_id == user_id)
    Certificate.create(
        account_id=user,
        certificate_number=certificate_id,
        factory_name=company_name,
        start_date=start_time,
        end_date=end_time,
        total_emission=amount,
        issue_date=issue_date,
        created_date=datetime.now(),
        transaction_hash=transaction_hash[2:]
        if transaction_hash.startswith("0x")
        else transaction_hash,
        transaction_date=transaction_date,
        certificate_address=certificate_address,
    )


def certificate_verification_attempt_create(
    certificate_id: str, total_emission: float, status: bool
) -> None:
    """
    Adds a certificate verification attempt to the database. Uses datetime.now() for the time.
    Assumes that the certificate_id provided is valid
    """
    certificate = Certificate.get(Certificate.certificate_number == certificate_id)
    CertificateVerificationAttempt.create(
        certificate_number=certificate,
        total_emission=total_emission,
        success=status,
        verified_time=datetime.now(),
    )


def certificate_get_data(certificate_id: str) -> dict:
    """
    Returns the data of the certificate with the given certificate_id.
    Creates a deepcopy of the data to prevent modification.
    """
    return deepcopy(
        Certificate.get(Certificate.certificate_number == certificate_id).__data__
    )


def database_setup(*, drop_tables=False):
    psql_db.connect()
    if drop_tables:
        psql_db.drop_tables([User, Certificate, CertificateVerificationAttempt])
    psql_db.create_tables([User, Certificate, CertificateVerificationAttempt])

    psql_db.execute_sql(
        "COMMENT ON COLUMN certificate.created_date IS 'When it was created on the HCEVP backend';"
    )
    psql_db.execute_sql(
        "COMMENT ON COLUMN certificate.transaction_date IS 'When the transaction was generated on the blockchain';"
    )
    psql_db.execute_sql(
        "COMMENT ON COLUMN certificate.certificate_address IS 'Ethereum address of the certificate without the 0x prefix';"
    )
    psql_db.execute_sql(
        "COMMENT ON COLUMN certificate.transaction_hash IS 'Transaction address that created the certificate without the 0x prefix';"
    )
