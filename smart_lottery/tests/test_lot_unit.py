"""Unit testing of contract
"""

from brownie import Lottery, accounts, network, config
import pytest
from web3 import Web3
from scripts.interact_lottery import b_victim, start_lot
from scripts.utils import LOCAL_BLOCKCHAINS, get_account
from scripts.deploy import deploy_lot


def test_get_fee():
    """test the init fee."""
    net = network.show_active()
    if net not in LOCAL_BLOCKCHAINS:
        pytest.skip()

    lot = deploy_lot()
    fee_dif = lot.getEntranceFee() - Web3.toWei(0.0025, "ether")
    assert fee_dif == 0


def test_enter():
    """test if you can enter the game``"""
    net = network.show_active()
    if net not in LOCAL_BLOCKCHAINS:
        pytest.skip()
    # Arrange
    acc = get_account()
    lot = deploy_lot()
    start_lot()
    # Act
    b_victim()
    # Assert
    assert lot.victims(0) == acc
    assert lot.lot_state() == 1
