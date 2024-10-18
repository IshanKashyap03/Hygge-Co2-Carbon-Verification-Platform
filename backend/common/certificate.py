# TODO: Refactor this file to allow for multiple contracts to be deployed and used
# TODO: Refactor to remove globals
import json
from pathlib import Path
from typing import Final

from eth_tester import EthereumTester
from eth_typing import ChecksumAddress
from web3 import EthereumTesterProvider, Web3
from web3.middleware import geth_poa_middleware


from backend.common.config import (
    CONTRACT_ADDRESS_AMOY,
    ENV_ACCOUNT_ADDRESS,
    PRIVATE_KEY,
    AMOY_URL
)
from backend.common.logger import logger

ETHEREUM_TRANSACTION_SUCCESS: Final[int] = 1

# Module variables
web3: Web3 | None = None
contract = None
ACCOUNT_ADDRESS: ChecksumAddress | None = None


def setup_certificate_module():
    global web3, contract, ACCOUNT_ADDRESS
    assert web3 is None, "Module already initialized"

    # Connect to Amoy Testnet
    provider = Web3.HTTPProvider(AMOY_URL)
    web3 = Web3(provider)

    # adding middleware to tell web3 that we are dealing with a Proof of Authority chain (Polygon)
    web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    # Check connection
    if not web3.is_connected():
        logger.critical("Failed to connect to Amoy Testnet")
        raise Exception("Failed to connect to Amoy Testnet")

    # Set account
    ACCOUNT_ADDRESS = (
        web3.to_checksum_address(ENV_ACCOUNT_ADDRESS)
        if ENV_ACCOUNT_ADDRESS
        else web3.eth.account.from_key(PRIVATE_KEY).address
    )
    assert ACCOUNT_ADDRESS is not None, "Failed to set account"

    logger.info(f"{ACCOUNT_ADDRESS = }")

    contract = create_contract(CONTRACT_ADDRESS_AMOY, ACCOUNT_ADDRESS)


def hash_data(*args: str) -> bytes:
    return bytes(Web3.solidity_keccak(["string"] * len(args), args))


def create_contract(contract_address: str | None, deployer_address: str):
    logger.info(f"{contract_address}")
    assert web3 is not None, "Module not initialized"

    # Find the path directly as otherwise it is very unreliable
    path = Path(__file__).resolve().parent / "contract" / "CertificateFactory-abi.json"

    with open(path, "r") as file:
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
    logger.info(
        "Deployer address:{deployer_address}", deployer_address=deployer_address
    )

    # Build the transaction
    tx = CertificateFactory.constructor().build_transaction(
        {
            "from": deployer_address,
            "nonce": web3.eth.get_transaction_count(deployer_address),
            "maxFeePerGas": web3.to_wei("25", "gwei"), 
            "maxPriorityFeePerGas": web3.to_wei("25", "gwei")
        }
    )
    gas = web3.eth.estimate_gas(tx)
    tx["gas"] = gas

    # Sign the transaction
    signed_tx = web3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)

    # Send the signed transaction
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

    logger.info("Create contract {receipt}", receipt=receipt)
    deployed_addr = receipt["contractAddress"]
    logger.info("Contract deployed at {deployed_addr}", deployed_addr=deployed_addr)

    return web3.eth.contract(address=deployed_addr, abi=contract_abi)


def create_certificate(computed_hash: bytes, verification_hash: bytes):
    """
    Create a certificate on the blockchain
    """
    assert web3 is not None, "Module not initialized"
    assert contract is not None, "Module not initialized"
    assert ACCOUNT_ADDRESS is not None, "Module not initialized"

    # Fetch the current base fee from the latest block
    latest_block = web3.eth.get_block("latest")
    base_fee = latest_block["baseFeePerGas"]

    # Set a reasonable max priority fee and max fee per gas
    max_priority_fee = web3.to_wei("25", "gwei")
    max_fee = base_fee + max_priority_fee

    # Build transaction
    nonce = web3.eth.get_transaction_count(ACCOUNT_ADDRESS)
    txn = contract.functions.createCertificate(
        (computed_hash), (verification_hash)
    ).build_transaction(
        {
            "from": ACCOUNT_ADDRESS,
            "nonce": nonce,
            "maxFeePerGas": max_fee,
            "maxPriorityFeePerGas": max_priority_fee,
        }
    )
    gas = web3.eth.estimate_gas(txn)
    txn["gas"] = gas

    signed_txn = web3.eth.account.sign_transaction(txn, PRIVATE_KEY)

    # Based on the version of Python not the package it uses different attribute names
    try:
        get_raw_transaction = signed_txn.rawTransaction
    except AttributeError:
        get_raw_transaction = signed_txn.raw_transaction

    tx_hash = web3.eth.send_raw_transaction(get_raw_transaction)

    logger.info(f"Certificate creation transaction hash: {web3.to_hex(tx_hash)}")
    logger.info("Waiting for transaction to be mined...")
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    logger.info("Certificate creation transaction receipt: {receipt}", receipt=receipt)
    return receipt


def verify_certificate(verification_hash: bytes) -> bool:
    assert contract is not None, "Module not initialized"
    logger.info(
        "Verifying certificates using verification_hash={verification_hash}",
        verification_hash=verification_hash,
    )
    status = contract.functions.verifyCertificate(verification_hash).call()
    logger.info("verify_certificates's status={status}", status=status)
    return status
