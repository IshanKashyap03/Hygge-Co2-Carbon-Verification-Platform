from dotenv import load_dotenv
import os
from typing import Final, Optional


load_dotenv()
ConstEnvAlias = Final[Optional[str]]

# Basic environment variables
INFURA_URL: ConstEnvAlias = os.getenv("INFURA_URL")
ENV_ACCOUNT_ADDRESS: ConstEnvAlias = os.getenv("ACCOUNT_ADDRESS")
CONTRACT_ADDRESS: ConstEnvAlias = os.getenv("CONTRACT_ADDRESS")

# Setup private key
# TODO: Use vault
__PRIVATE_KEY = os.getenv("PRIVATE_KEY")
PRIVATE_KEY: Final[str] = (
    __PRIVATE_KEY
    if __PRIVATE_KEY
    else "0x58d23b55bc9cdce1f18c2500f40ff4ab7245df9a89505e9b1fa4851f623d241d"
)
