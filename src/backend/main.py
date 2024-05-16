from web3 import Web3
import hashlib
import json

# Connect to Ethereum node using Infura
infura_url = 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'
web3 = Web3(Web3.HTTPProvider(infura_url))

# Check connection
if not web3.isConnected():
    raise Exception("Failed to connect to Ethereum")

# Replace with your contract's ABI and address
contract_address = '0xYourContractAddress'
with open('build/CertificateFactory.abi', 'r') as file:
    contract_abi = json.load(file)

# Create the contract instance
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# Define account and private key for sending transactions
account = '0xYourAccountAddress'
private_key = '0xYourPrivateKey'

# Function to create a certificate
def create_certificate(start_time, end_time, company_name, amount):
    # Hash the sensitive data
    data_string = f"{start_time}{end_time}{company_name}"
    computed_hash = hashlib.sha256(data_string.encode()).hexdigest()
    computed_hash_bytes = web3.toBytes(hexstr=computed_hash)
    
    nonce = web3.eth.getTransactionCount(account)
    txn = contract.functions.createCertificate(computed_hash_bytes, amount).buildTransaction({
        'chainId': 1,  # Mainnet
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = web3.eth.account.signTransaction(txn, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(f'Transaction hash: {web3.toHex(tx_hash)}')
    return tx_hash

# Example usage
start_time = 1715836780
end_time = 1715836780
company_name = "YourCompanyName"
amount = 100

# Create a certificate
tx_hash = create_certificate(start_time, end_time, company_name, amount)
print(f'Certificate creation transaction hash: {tx_hash}')
