"""Helper functions
"""

from brownie import MockV3Aggregator, accounts, network, config
from icecream import ic
from web3 import Web3


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


def get_feed_address() -> str:
    """Get the eth price feed address
    depening on the network you are on.

    Returns:
        str: price feed address
    """
    net = network.show_active()
    if net == "development":
        print("Deploying Mocks..")
        eth_sum = Web3.toWei(2000, "ether")
        if len(MockV3Aggregator) > 0:
            MockV3Aggregator.deploy(
                18,
                eth_sum,
                {"from": accounts[0]},
            )
        ic(len(MockV3Aggregator))
        feed = MockV3Aggregator.address
    else:
        feed = config["networks"][net]["eth_feed"]
    return feed
