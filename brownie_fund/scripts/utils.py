"""Helper functions
"""

from brownie import accounts, network, config
from icecream import ic


def get_account() -> str:
    """Checks for network and returns account public key.
    if on Ganache, the native generated first account ist returned.
    On testnet, the account stored in .env.
    """
    net = network.show_active()
    print("WTF mate?! You're sailing on the {} networq!".format(net))
    if net == "development":
        ic(accounts[0])
        acc = accounts[0]
    else:
        acc = accounts.add(config["wallets"]["from_key"])
    return acc
