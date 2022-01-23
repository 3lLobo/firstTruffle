"""Test the Lottery contract.
"""

from brownie import Lottery, accounts, config, network
from web3 import Web3
from icecream import ic

from scripts.deploy import deploy_lot
from scripts.utils import get_account


def test_getEntranceFee():
    """Test the getEntranceFee function."""
    lottery = deploy_lot()
    acc = get_account
    ic(lottery.getEthPrice())
    ic(lottery.getEntranceFee())
    # Check if price is in plausible range.
    assert lottery.getEntranceFee() > Web3.toWei(.0014, 'ether')
    assert lottery.getEntranceFee() < Web3.toWei(.0033, 'ether')
