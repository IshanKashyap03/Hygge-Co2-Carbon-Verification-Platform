import peewee as sql
from config import DATABASE_NAME, DATABASE_USER

psql_db = sql.PostgresqlDatabase(DATABASE_NAME, user=DATABASE_USER)

class BaseModel(sql.Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = psql_db

class TransactionStatus:
    NOT_STARTED = 'not_started'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

    choices = [
        (NOT_STARTED, 'Not Started'),
        (IN_PROGRESS, 'In Progress'),
        (COMPLETED, 'Completed')
    ]


class Users(BaseModel):
    id = sql.BigAutoField(primary_key=True)
    account_id = sql.CharField(max_length=50, unique=True, null=False)

class Certificates(BaseModel):
    id = sql.BigAutoField(primary_key=True)
    account_id = sql.ForeignKeyField(Users, backref='certificates', to_field="account_id")
    certificate_number = sql.CharField(max_length=50, unique=True, null=False)
    factory_name = sql.CharField(max_length=255, null=False)
    start_date = sql.TimestampField(null=False)
    end_date = sql.TimestampField(null=False)
    total_emission = sql.FloatField(null=False)
    issue_date = sql.TimestampField(null=False)
    created_date = sql.TimestampField(null=False)
    transaction_date = sql.TimestampField(null=False)
    transaction_status = sql.CharField(choices=TransactionStatus.choices, default=TransactionStatus.NOT_STARTED)
    address = sql.CharField(max_length=40, null=True, default=None)
    transaction_hash = sql.CharField(max_length=64, null=True, default=None)

class CertificateVerificationAttempts(BaseModel):
    certificate_number = sql.ForeignKeyField(Certificates, backref='certificate_verification_attempts', to_field="certificate_number")
    total_emission = sql.FloatField(null=False)
    verified_time = sql.TimestampField(null=False)
    success = sql.BooleanField(null=False)

psql_db.connect()
psql_db.create_tables([Users, Certificates, CertificateVerificationAttempts])

psql_db.execute_sql("COMMENT ON COLUMN certificates.created_date IS 'When it was created on the HCEVP backend';")
psql_db.execute_sql("COMMENT ON COLUMN certificates.transaction_date IS 'When it was created on the HCEVP backend';")
psql_db.execute_sql("COMMENT ON COLUMN certificates.address IS 'Ethereum address of the certificate without the 0x prefix';")
psql_db.execute_sql("COMMENT ON COLUMN certificates.transaction_hash IS 'Transaction address that created the certificate without the 0x prefix';")
