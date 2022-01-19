from brownie import FundMe, Wei
from scripts.utils import get_account, get_feed_address
from icecream import ic


def fund():
    """Fund the contract.
    Use the fund function from FundMe contract to deploy eth.
    """
    fundme = FundMe[-1]
    acc = get_account()
    e_fee = fundme.getEntranceFee()
    ic(Wei(e_fee).to('ether'))
    fundme.fund({"from": acc, "value": 10000 * e_fee})
    print("Your account balance is:", Wei(acc.balance()).to('ether'))


def withdraw():
    """Withdraw contract value to owner account."""
    fundme = FundMe[-1]
    acc = get_account()
    fundme.withdraw({'from': acc})
    print("Your account balance is now:", Wei(acc.balance()).to('ether'))


def main():
    """Main App"""
    fund()
    withdraw()
