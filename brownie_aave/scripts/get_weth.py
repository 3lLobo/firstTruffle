"""Mint wether by borrowing eth.
"""

from scripts.utils import get_account
from brownie import interface, network, config
from web3 import Web3


def get_weth():
    """get weth function"""
    acc = get_account()
    print(acc)
    print("ETH balance: ", Web3.fromWei(acc.balance(), "ether"))
    weth = interface.WethInterface(
        config["networks"][network.show_active()]["weth_token"]
    )
    txx = weth.deposit({"from": acc, "value": 1 * 10 ** 18})
    txx.wait(1)
    print("Recieved weth!")
    print("WETH balance: ", weth.balanceOf(acc))
    print("ETH balance: ", Web3.fromWei(acc.balance(), "ether"))
    return txx


def main():
    get_weth()
