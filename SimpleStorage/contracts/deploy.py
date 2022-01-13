"""Deployment script.
"""
import os
from dotenv import load_dotenv
import solcx
import json
from web3 import Web3
from icecream import ic

load_dotenv()
solcx.install_solc("0.8.11")


with open("./SimpleStorage/contracts/SimpleStorage.sol", "r") as f:
    simple_storage_file = f.read()
    # print(simple_storage_file)

comp_sol = solcx.compile_standard(
    {
        "language": "Solidity",
        "sources": {
            "SimpleStorage.sol": {
                "content": simple_storage_file,
            },
        },
        "settings": {
            "outputSelection": {
                "*": {
                    "*": [
                        "abi",
                        "metadata",
                        "evm.bytecode",
                        "evm.sourceMap",
                    ]
                }
            }
        },
    },
    solc_version="0.8.11",
)
# print(comp_sol)

with open("./compiled_sol.json", "w") as f:
    json.dump(comp_sol, f)

# Bytecode
bytecode = comp_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"][
    "bytecode"
]["object"]

# ABI
abi = comp_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# Web3
endpoint_html = os.getenv("CHAIN_HTML")
w3 = Web3(Web3.HTTPProvider(endpoint_html))
chain_id = int(os.getenv("CHAIN_ID"))
myaddress = os.getenv("ETH_ADRS")
# second_address = "0x44abcdaf50e7cf79aaadF860e7c2C89BF8b5864d"
priv_key = os.getenv("PRIV_KEY")

# Create contract
SimpleStorage = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(SimpleStorage)

# lastest transaction
nonce = w3.eth.getTransactionCount(myaddress)
ic(nonce)

# Transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "from": myaddress,
        "nonce": nonce,
        "gasPrice": 20000000000,
    }
)

# ic(transaction)
signd_txn = w3.eth.account.sign_transaction(transaction, priv_key)
# ic(signd_txn)

# Send transaction
tx_hash = w3.eth.send_raw_transaction(signd_txn.rawTransaction)
# ic(tx_hash)
tx_recipt = w3.eth.wait_for_transaction_receipt(tx_hash)
# ic(tx_recipt)

# Work with the contract
ss_contract = w3.eth.contract(address=tx_recipt.contractAddress, abi=abi)
ic(ss_contract.functions.retrieve_view().call())

store_tx = ss_contract.functions.i_store(b"11Lobo").buildTransaction(
    {
        "chainId": chain_id,
        "from": myaddress,
        "nonce": nonce + 1,
        "gasPrice": 20000000000,
    }
)
sign_store = w3.eth.account.sign_transaction(store_tx, priv_key)
send_store = w3.eth.send_raw_transaction(sign_store.rawTransaction)
store_reciept = w3.eth.wait_for_transaction_receipt(send_store)
# ic(store_reciept)

ic(ss_contract.functions.retrieve_view().call())
