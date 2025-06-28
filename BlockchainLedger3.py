#!/usr/bin/env python
# coding: utf-8

# In[1]:


from web3 import Web3

# Connect to local Ganache blockchain (port 8545)
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Check connection
if web3.is_connected():
    print("✅ Connected to Ganache successfully!")
else:
    print("❌ Connection failed. Ensure Ganache is running.")


# In[3]:


# Replace with your actual deployed contract address
contract_address = Web3.to_checksum_address("0xc4524bbc7ad3dabcd9b176fb2a99dea71226a43b")

# Paste your ABI (this should be a list of dictionaries, not nested)
abi = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "internalType": "uint256", "name": "timestamp", "type": "uint256"},
            {"indexed": False, "internalType": "string", "name": "unitID", "type": "string"},
            {"indexed": False, "internalType": "string", "name": "gpsLocation", "type": "string"},
            {"indexed": False, "internalType": "string", "name": "fireSystemStatus", "type": "string"},
            {"indexed": False, "internalType": "uint256", "name": "fuelLevel", "type": "uint256"}
        ],
        "name": "DataStored",
        "type": "event"
    },
    {
        "inputs": [
            {"internalType": "string", "name": "_unitID", "type": "string"},
            {"internalType": "string", "name": "_gpsLocation", "type": "string"},
            {"internalType": "string", "name": "_fireSystemStatus", "type": "string"},
            {"internalType": "uint256", "name": "_fuelLevel", "type": "uint256"}
        ],
        "name": "storeData",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "name": "dataRecords",
        "outputs": [
            {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
            {"internalType": "string", "name": "unitID", "type": "string"},
            {"internalType": "string", "name": "gpsLocation", "type": "string"},
            {"internalType": "string", "name": "fireSystemStatus", "type": "string"},
            {"internalType": "uint256", "name": "fuelLevel", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "index", "type": "uint256"}
        ],
        "name": "getRecord",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"},
            {"internalType": "string", "name": "", "type": "string"},
            {"internalType": "string", "name": "", "type": "string"},
            {"internalType": "string", "name": "", "type": "string"},
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "getTotalRecords",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "MAX_ENTRIES",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {"internalType": "address", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

# Load the smart contract
contract = web3.eth.contract(address=contract_address, abi=abi)

# Set default account to the first Ganache address
web3.eth.default_account = web3.eth.accounts[0]

print(f"✅ Smart contract loaded at: {contract_address}")


# In[4]:


# Send a test transaction to store data
txn = contract.functions.storeData(
    "TEST001",
    "GPS_COORDS_123",
    "OK",
    80
).transact({
    'from': web3.eth.default_account,
    'gas': 1000000
})

# Wait for the transaction to be mined
web3.eth.wait_for_transaction_receipt(txn)
print("✅ Dummy IoT data stored on blockchain!")


# In[5]:


# Check how many records are stored
total_records = contract.functions.getTotalRecords().call()
print(f"📦 Total Records Stored: {total_records}")

# Get the first record
record = contract.functions.getRecord(0).call()
print("📋 First Record:", record)


# In[ ]:




