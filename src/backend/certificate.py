from web3 import Web3, EthereumTesterProvider
from eth_tester import EthereumTester
import json
from config import INFURA_URL, PRIVATE_KEY, ENV_ACCOUNT_ADDRESS, CONTRACT_ADDRESS
from logger import logger


# Connect to Ethereum node using Infura
provider = Web3.HTTPProvider(INFURA_URL) if INFURA_URL else EthereumTesterProvider()
web3 = Web3(provider)
tester = EthereumTester()

# Check connection
if not web3.is_connected():
    logger.critical("Failed to connect to Ethereum")
    raise Exception("Failed to connect to Ethereum")


# Set account
ACCOUNT_ADDRESS = (
    web3.to_checksum_address(ENV_ACCOUNT_ADDRESS)
    if ENV_ACCOUNT_ADDRESS
    else tester.add_account(PRIVATE_KEY)
)
logger.info(f"{ACCOUNT_ADDRESS = }")
if not INFURA_URL:  # This means we are using the tester provider
    logger.info("Sending 1 ether to the account for testing purposes")
    account1 = tester.get_accounts()[0]
    txn = web3.eth.send_transaction(
        {
            "from": account1,
            "to": ACCOUNT_ADDRESS,
            "value": web3.to_wei(1, "ether"),
        }
    )


def hash_data(*args: str) -> str:
    logger.info("Hashing {args}", args=args)
    return Web3.solidity_keccak(["string"] * len(args), args).hex()


def create_contract(contract_address: str | None, deployer_address: str):
    with open("../contract/CertificateFactory-abi.json", "r") as file:
        contract_abi = json.load(file)

    logger.info(
        "Contract address: {contract_address}", contract_address=contract_address
    )

    if contract_address:
        logger.info("Using existing contract")
        return web3.eth.contract(
            address=web3.to_checksum_address(contract_address),
            abi=contract_abi,
        )
    logger.info("Creating new contract")

    # Create a new contract for testing purposes
    with open("../contract/CertificateFactory-bytecode.bin") as f:
        contract_byte_code = f.read().strip()

    CertificateFactory = web3.eth.contract(
        bytecode=contract_byte_code, abi=contract_abi
    )
    deployer_address = web3.to_checksum_address(deployer_address)
    logger.info(f"{deployer_address = }")
    tx = CertificateFactory.constructor().build_transaction(
        {
            "from": deployer_address,
            "nonce": web3.eth.get_transaction_count(deployer_address),
            "gas": 2000000,  # TODO: For future, better estimate gas than use hardcoded value
            "gasPrice": web3.to_wei("50", "gwei"),
        }
    )
    # Sign the transaction
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)

    # Send the signed transaction
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    logger.info("Create contract {receipt}", receipt=receipt)
    deployed_addr = receipt["contractAddress"]
    logger.info("Contract deployed at {deployed_addr}", deployed_addr=deployed_addr)

    return web3.eth.contract(address=deployed_addr, abi=contract_abi)


contract = create_contract(CONTRACT_ADDRESS, ACCOUNT_ADDRESS)


def create_certificate(computed_hash: str, verification_hash: str):
    """
    Create a certificate on the blockchain
    """
    nonce = web3.eth.get_transaction_count(ACCOUNT_ADDRESS)
    txn = contract.functions.createCertificate(
        computed_hash, verification_hash
    ).build_transaction(
        {
            "from": ACCOUNT_ADDRESS,
            "gas": 2000000,
            "gasPrice": web3.to_wei("50", "gwei"),
            "nonce": nonce,
        }
    )

    signed_txn = web3.eth.account.sign_transaction(txn, PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    logger.info(f"Certificate creation transaction hash: {web3.to_hex(tx_hash)}")
    logger.info("Waiting for transaction to be mined...")
    logger.info(web3.eth.wait_for_transaction_receipt(tx_hash))
    return web3.eth.get_transaction(tx_hash)


def verify_certificate(verification_hash: str) -> bool:
    logger.info(
        "Verifying certificates using verification_hash={verification_hash}",
        verification_hash=verification_hash,
    )
    status = contract.functions.verifyCertificate(verification_hash).call()
    logger.info("verify_certificates's status={status}", status=status)
    return status
