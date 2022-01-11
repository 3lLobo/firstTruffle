"""Deployment script.
"""
import solcx
import json

solcx.install_solc("0.8.0")


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
    solc_version="0.6.0",
)
# print(comp_sol)

with open("./compiled_sol.json", "w") as f:
    json.dump(comp_sol, f)
