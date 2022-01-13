"""Brownie deploy scirpt
"""

from audioop import add
from json import load
from multiprocessing.connection import wait
from brownie import accounts, config, SimpleStorage, network
import os
from icecream import ic


def deploy_sstorage():
    account = get_account()
    # print(accounts.load('3lLobo'))
    # account = accounts.add(config['wallets']['from_key'])
    ic(account)
    simple_store = SimpleStorage.deploy({"from": account})
    stored_val = simple_store.retrieve()
    ic(stored_val)
    transaction = simple_store.store2("11Lobo", {"from": account})
    transaction.wait(1)
    new_stored_val = simple_store.retrieve()
    ic(new_stored_val)


def get_account() -> str:
    """Checks for network and returns account public key.
    if on Ganache, the native generated first account ist returned.
    On testnet, the account stored in .env.
    """
    net = network.show_active()
    print("WTF mate?! You're sailing on the {} networq!".format(net))
    if net == "developement":
        acc = accounts[0]
    else:
        acc = accounts.add(config["wallets"]["from_key"])
    return acc


def main():
    print("Hiiigh!")
    deploy_sstorage()


if __name__ == "__main__":
    main()
