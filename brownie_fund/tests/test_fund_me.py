"""Test the FundMe function
"""

from brownie import network, exceptions, Wei
import pytest
from scripts.deploy import deploy_fund
from scripts.utils import get_account, LOCAL_BLOCKCHAINS, FORKED_LOCAL_CHAIN


def test_can_fund_and_withdraw():
    """Test if you can fund and withdraw funds from and to the contract."""
    acc = get_account()
    fund = deploy_fund()
    e_fee = fund.getEntranceFee() + 11
    print(
        "Funding: ETH {:.3} or USD {:.3}".format(
            Wei(e_fee).to("ether"),
            fund.getConversionRate(e_fee) / 10 ** 18,
        ),
    )
    tx = fund.fund({"from": acc, "value": e_fee})
    tx.wait(1)
    # Check if the ammount funded was recived in good order
    assert fund.addressToAmountFunded(acc.address) == e_fee

    tx2 = fund.withdraw({"from": acc})
    tx2.wait(1)
    # Check if the mapping was reset as a result of withdrawinf the funds
    assert fund.addressToAmountFunded(acc.address) == 0


def test_only_owner_can_withdraw():
    """The name says it all."""
    if network.show_active() not in LOCAL_BLOCKCHAINS+FORKED_LOCAL_CHAIN:
        pytest.skip("Test Only on local blockchains!")
    # acc = get_account()
    fund = deploy_fund()
    bad_acc = get_account(3)

    with pytest.raises(exceptions.VirtualMachineError):
        fund.withdraw({"from": bad_acc})
