"""Helper functions
"""

from brownie import MockV3Aggregator, accounts, network, config, Contract
from icecream import ic
from web3 import Web3

DECIMALS = 8
START_PRICE = 20e11
LOCAL_BLOCKCHAINS = ["development", "ganachewin11"]
FORKED_LOCAL_CHAIN = ["mainnet-fork", "dev-fork"]


def get_account(acc_ind: int = 0) -> str:
    """Checks for network and returns account public key.
    if on Ganache, the native generated first account ist returned.
    On testnet, the account stored in .env.

    Args:
        acc_ind[int]: index of the local account. Default is the first one.
    """
    net = network.show_active()
    print("WTF mate?! You're sailing on the {} networq!".format(net))
    if net in LOCAL_BLOCKCHAINS + FORKED_LOCAL_CHAIN:
        ic(accounts[acc_ind])
        acc = accounts[acc_ind]
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
    if net in LOCAL_BLOCKCHAINS:
        print("Deploying Mocks..")
        # eth_sum = Web3.toWei(2000, "ether")
        if len(MockV3Aggregator) >= 0:
            MockV3Aggregator.deploy(
                DECIMALS,
                START_PRICE,
                {"from": accounts[0]},
            )
        feed = MockV3Aggregator[-1].address
    else:
        feed = config["networks"][net]["eth_feed"]
    return feed
