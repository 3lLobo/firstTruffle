"""Eternalize your mates on the blocqchain
"""

import imp
from brownie import SimpleStorage, accounts
from scripts.brownie_deploy import get_account
from icecream import ic


def add_mate(name, years):
    """Add your mate to the blocqchain.

    Args:
        name (string): the name you want to add to storage
    """
    ss_contract = SimpleStorage[-1]
    acc = get_account()
    transction = ss_contract.addFriend(name, years, {"from": acc})
    transction.wait(1)
    ic(ss_contract.name2number(name))


def main():
    """Main app"""
    mate = "Nuka <3"
    years = 111 add_mate(mate, years=years)
