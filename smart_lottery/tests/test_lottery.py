"""Test the Lottery contract.
"""

from brownie import Lottery, accounts, config, network
from web3 import Web3
from icecream import ic


def test_getEntranceFee():
    """Test the getEntranceFee function."""
    acc = accounts[0]
    lottery = Lottery.deploy(
        config["networks"][network.show_active()]["eth_feed"],
        {
            "from": acc,
        },
    )
    ic(lottery.getEthPrice())
    ic(lottery.getEntranceFee())
    # Check if price is in plausible range.
    assert lottery.getEntranceFee() > Web3.toWei(.014, 'ether')
    assert lottery.getEntranceFee() < Web3.toWei(.033, 'ether')
