"""function to deploy a NFT
"""

from brownie import Contract, config, AdvancedNFT, network
from typing import Dict
from scripts.utils import fund_link, get_account, get_contract


def deploy_adv_nft(ntf_uri: Dict) -> Contract:
    """Deploy youre NFT

    Args:
        ntf_uri (Dict): Metadata for the NFT

    Returns:
        Contract: Transaction of the deployment
    """
    acc = get_account()
    nft = AdvancedNFT.deploy(
        get_contract("vrf"),
        get_contract("link"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": acc},
    )
    # tx.wait(1)
    fund_link(nft)
    tx2 = nft.createNFT(ntf_uri, {"from": acc})
    tx2.wait(1)
    print('NFT createt! {} times minted.'.format(nft.tokenCount()))


    return nft, tx2


def mintNFT():
    """Mint a NFT"""
    pass


def main():
    """Main app"""
    nft_uri = "res/uri/goku.json"
    deploy_nft(nft_uri)
