"""Deploy contracts
"""
from brownie import FundMe, MockV3Aggregator, accounts, network, config, Contract
from scripts.utils import get_account, get_feed_address
from icecream import ic


def deploy_fund() -> Contract:
    """Deploy the FundMe contract.

    Returns:
        Contract: brownie interace for the FundMe contract.
    """
    acc = get_account()
    feed_address = get_feed_address()
    fund_me = FundMe.deploy(
        feed_address,
        {"from": acc},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    # fund_me.wait(1)
    print("Contract deployed to address: {}".format(fund_me.address))
    return fund_me

def main():
    """Main app"""
    _ = deploy_fund()
