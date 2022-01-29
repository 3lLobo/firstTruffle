"""Helper functions
"""

from code import interact
import string
from brownie import (
    MockV3Aggregator,
    VRFCoordinatorMock,
    LinkToken,
    accounts,
    network,
    interface,
    config,
    Contract
    
)
from brownie.network.contract import ProjectContract
from eth_account import Account
from eth_typing import Address
from icecream import ic
from web3 import Web3


DECIMALS = 8
START_PRICE = 20e11
LOCAL_BLOCKCHAINS = ["development", "ganachewin11"]
FORKED_LOCAL_CHAIN = ["mainnet-fork", "dev-fork"]


def get_account(acc_idx: int = 0, brownie_id: int = None) -> str:
    """Checks for network and returns account public key.
    if on Ganache, the native generated first account ist returned.
    On testnet, the account stored in .env.

    Args:
        acc_idx[int]: index of the local account. Default is the first one.
        bronie_id[int]: Id of the account stored in brownie.
    """
    net = network.show_active()
    print("WTF mate?! You're sailing on the {} networq!".format(net))

    if brownie_id:
        return accounts.load(brownie_id)

    if net in LOCAL_BLOCKCHAINS + FORKED_LOCAL_CHAIN:
        ic(accounts[acc_idx])
        return accounts[acc_idx]
    else:
        return accounts.add(config["wallets"]["from_key"])


c_map = {
    "eth_feed": MockV3Aggregator,
    "vrf": VRFCoordinatorMock,
    "link": LinkToken,
}


def get_contract(c_name: string) -> ProjectContract:
    """Returs the contract defined in brownie config.
    If no contract is defined, a moch version is deployed.

    Args:
        c_name (string): contract name

    Returns:
        ProjectContract: most recent deployed contract or mock.
    """
    c_type = c_map[c_name]
    net = network.show_active()

    if net in LOCAL_BLOCKCHAINS:
        if len(c_type) <= 0:
            # MockV3Aggregator.length
            deploy_mocks()
        contract = c_type[-1]
    else:
        c_address = config["networks"][net][c_name]
        contract = Contract.from_abi(c_type._name, c_address, c_type.abi)

    return contract


def deploy_mocks():
    """Deploy MockV3Aggregator"""
    acc = get_account()
    MockV3Aggregator.deploy(DECIMALS, START_PRICE, {"from": acc})
    print("Deployed MockV3Agg!")
    link_mock = LinkToken.deploy({"from": acc})
    print("Deployed LinkMock!")
    vrf = VRFCoordinatorMock.deploy(link_mock.address, {"from": acc}),
    print("Deployed VRF!")
    # fund_link(vrf, acc, link_mock)
    # print("Funded VRF1")


def fund_link(
    c_address: Address,
    acc: Account = None,
    token: Address = None,
    value: int = 10 ** 17,
):
    """Fund the given contract with certain ammount of token.

    Args:
        c_address (Address): contract address
        acc (Account, optional): Emmitting account. Defaults to None.
        link (Address, optional): Toke address. Defaults to None.
        value (int, optional): Value to be transferes. Defaults to 10**17.
    
    Returns:
        Transaction confirmation
    """
    acc = acc if acc else get_account()
    token = token if token else get_contract("link")
    # tx = token.transfer(c_address, value+111, {"from": acc})
    link_interface = interface.LinkTokenInterface(token.address)
    tx = link_interface.transfer(c_address, value, {"from": acc})
    tx.wait(1)
    print("Funded contract!")
    
    return tx
