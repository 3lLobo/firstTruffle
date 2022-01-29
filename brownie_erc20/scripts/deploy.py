"""Deploy script"""
from web3 import Web3
from brownie import accounts, network, WolfCoin
from scripts.utils import get_account

INIT_SUPPLY = 10 ** 11


def deploy_token():
    """Deploy the custom token."""
    acc = get_account()
    wolf_coin = WolfCoin.deploy(INIT_SUPPLY, {"from": acc})

def main():
    """Main app.
    """
    deploy_token()