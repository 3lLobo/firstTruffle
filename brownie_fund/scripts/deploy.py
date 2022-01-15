"""Deploy contracts
"""
from brownie import FundMe, accounts, network
from scripts.utils import get_account



def deploy_fund():
    """Deploy the FundMe contract
    """
    acc = get_account()
    fund_me = FundMe.deploy({'from': acc}, publish_source=True)
    # TODO get api tokken on etherscan to verify.
    # fund_me.wait(1)
    print('Contract deployed to address: {}'.format(fund_me.address))


def main():
    """Main app
    """
    deploy_fund()
