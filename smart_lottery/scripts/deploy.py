"""Deploy the contracts.
"""

from black import main
from brownie import accounts, network, Lottery, config
from scripts.utils import get_account, get_contract


def deploy_lot():
    """Deploy the Lottery contract."""
    acc = get_account()
    net = network.show_active()
    lot = Lottery.deploy(
        get_contract("eth_feed").address,
        get_contract("vrf").address,
        get_contract("link").address,
        int(config["networks"][net]["fee"]),
        config["networks"][net]["keyhash"],
        {"from": acc},
        publish_source=config["networks"][net].get("verify", False),
    )
    print("Deployed Lottery!")
    return lot


def main():
    """Main app"""
    deploy_lot()
