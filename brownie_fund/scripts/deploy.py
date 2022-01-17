"""Deploy contracts
"""
from brownie import FundMe, accounts, network
from scripts.utils import get_account
from icecream import ic

def deploy_fund():
    """Deploy the FundMe contract"""
    acc = get_account()
    fund_me = FundMe.deploy(
        {"from": acc},
        publish_source=True,
    )
    # fund_me.wait(1)
    print("Contract deployed to address: {}".format(fund_me.address))


def main():
    """Main app"""
    deploy_fund()
