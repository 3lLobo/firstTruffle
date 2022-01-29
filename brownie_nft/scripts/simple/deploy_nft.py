"""function to deploy a NFT
"""

from brownie import Contract, config, SimpleNFT
from typing import Dict
from scripts.utils import get_account


def deployNFT(ntf_uri: Dict) -> Contract:
    """Deploy youre NFT

    Args:
        ntf_uri (Dict): Metadata for the NFT

    Returns:
        Contract: Transaction of the deployment
    """
    acc = get_account()
    nft = SimpleNFT.deploy(nft_uri, {"from": acc})
    tx = nft.createNFT(ntf_uri, {"from": acc})

    return tx


def mintNFT():
    """Mint a NFT"""
    pass


def main():
    """Main app"""
    nft_uri = "res/uri/goku.json"
    deployNFT(nft_uri)
    mintNFT()
