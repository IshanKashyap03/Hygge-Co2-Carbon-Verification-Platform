import os
from typing import Final, Optional

from dotenv import load_dotenv


def extract_env_var(env_var: str) -> str:
    value = os.getenv(env_var)
    if value is None:
        raise ValueError(f"{env_var} is required")
    return value


load_dotenv()
ConstEnvVariable = Final[Optional[str]]

# Basic environment variables
INFURA_URL: ConstEnvVariable = os.getenv("INFURA_URL")
AMOY_URL: ConstEnvVariable = os.getenv("AMOY_URL")
ENV_ACCOUNT_ADDRESS: ConstEnvVariable = os.getenv("ACCOUNT_ADDRESS")
CONTRACT_ADDRESS: ConstEnvVariable = os.getenv("CONTRACT_ADDRESS")
CONTRACT_ADDRESS_AMOY: ConstEnvVariable = os.getenv("CONTRACT_ADDRESS_AMOY")

# Setup private key
__PRIVATE_KEY = os.getenv("PRIVATE_KEY")
PRIVATE_KEY: Final[str] = (
    __PRIVATE_KEY
    if __PRIVATE_KEY
    else "0x58d23b55bc9cdce1f18c2500f40ff4ab7245df9a89505e9b1fa4851f623d241d"
)

# Logger details
LOGGER_DIAGNOSE: Final[bool] = True  # TODO: Update to this to False when in production
LOGGER_DIR: Final[str] = os.getenv("LOGGER_DIR") or ""

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
CERTIFICATE_DATA_BROKER_ID: Final[str] = extract_env_var("CERTIFICATE_DATA_BROKER_ID")
CERTIFICATE_PUBLISHER_TOPIC: Final[str] = extract_env_var("CERTIFICATE_PUBLISHER_TOPIC")
CERTIFICATE_PUBLISHER_ID: Final[str] = extract_env_var("CERTIFICATE_PUBLISHER_ID")
PAHO_QUALITY_OF_SERVICE_LEVEL_AT_MOST_ONCE: Final[int] = 2

# API Database Config
API_DATABASE_NAME: Final[str] = extract_env_var("DATABASE_NAME")
API_DATABASE_USER: Final[str] = extract_env_var("DATABASE_USER")
API_DATABASE_PASSWORD: Final[str] = extract_env_var("DATABASE_PASSWORD")
API_DATABASE_HOST: Final[str] = os.getenv("DATABASE_HOST", "localhost")
API_DATABASE_PORT: Final[int] = int(extract_env_var("DATABASE_PORT"))

# Publisher Database Config
PUBLISHER_DATABASE_NAME: Final[str] = extract_env_var("PUBLISHER_DATABASE_NAME")
PUBLISHER_DATABASE_USER: Final[str] = extract_env_var("PUBLISHER_DATABASE_USER")
PUBLISHER_DATABASE_PASSWORD: Final[str] = extract_env_var("PUBLISHER_DATABASE_PASSWORD")
PUBLISHER_DATABASE_HOST: Final[str] = os.getenv("PUBLISHER_DATABASE_HOST", "localhost")
PUBLISHER_DATABASE_PORT: Final[int] = int(extract_env_var("PUBLISHER_DATABASE_PORT"))

# JWT details
JWT_SECRET_KEY: Final[str] = extract_env_var("SECRET_KEY")
JWT_ALGORITHM: Final[str] = extract_env_var("ALGORITHM")
