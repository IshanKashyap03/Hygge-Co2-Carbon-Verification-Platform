from dotenv import load_dotenv
import os
from typing import Final, Optional


def extract_env_var(env_var: str) -> str:
    value = os.getenv(env_var)
    if value is None:
        raise ValueError(f"{env_var} is required")
    return value


load_dotenv()
ConstEnvVariable = Final[Optional[str]]

# Basic environment variables
INFURA_URL: ConstEnvVariable = os.getenv("INFURA_URL")
ENV_ACCOUNT_ADDRESS: ConstEnvVariable = os.getenv("ACCOUNT_ADDRESS")
CONTRACT_ADDRESS: ConstEnvVariable = os.getenv("CONTRACT_ADDRESS")

# Setup private key
__PRIVATE_KEY = os.getenv("PRIVATE_KEY")
PRIVATE_KEY: Final[str] = (
    __PRIVATE_KEY
    if __PRIVATE_KEY
    else "0x58d23b55bc9cdce1f18c2500f40ff4ab7245df9a89505e9b1fa4851f623d241d"
)


# MQTT broker details
CERTIFICATE_DATA_BROKER_URL: Final[str] = extract_env_var("CERTIFICATE_DATA_BROKER_URL")
CERTIFICATE_DATA_BROKER_PORT: Final[int] = int(
    extract_env_var("CERTIFICATE_DATA_BROKER_PORT")
)
CERTIFICATE_DATA_BROKER_USERNAME: Final[str] = extract_env_var(
    "CERTIFICATE_DATA_BROKER_USERNAME"
)
CERTIFICATE_DATA_BROKER_PASSWORD: Final[str] = extract_env_var(
    "CERTIFICATE_DATA_BROKER_PASSWORD"
)
CERTIFICATE_DATA_BROKER_TOPIC: Final[str] = extract_env_var(
    "CERTIFICATE_DATA_BROKER_TOPIC"
)

# Logger details
LOGGER_DIAGNOSE: Final[bool] = True  # TODO: Update to this to False when in production

# database details
DATABASE_NAME: ConstEnvVariable = os.getenv("DATABASE_NAME")
DATABASE_USER: ConstEnvVariable = os.getenv("DATABASE_USER")
