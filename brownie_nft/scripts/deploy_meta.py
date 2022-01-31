"""Create metadata for NFT.
"""
import requests
from metadata.nft_template import NFT_TEMPLATE
from scripts.advanced.deploy_adv_nft import main as deploy_adv_nft

import json
from icecream import ic
from brownie import AdvancedNFT, network
from brownie.network.gas.strategies import GasNowStrategy
from scripts.utils import LOCAL_BLOCKCHAINS, get_account

gas_strategy = GasNowStrategy("fast")

def create_meta(nft_path: str) -> str:
    """Create metadata for a NFT.

    Args:
        nft_path (str): image path

    Returns:
        [str]: json metadata path
    """
    nft_name = "Goku"
    nft_meta = NFT_TEMPLATE
    nft_meta["name"] = nft_name
    nft_meta["image"] = nft_path
    nft_meta_path = "./metadata/nft_{}.json".format(nft_name)

    with open(nft_meta_path, "w") as f:
        json.dump(nft_meta, f)

    return nft_meta_path


def upload2ipfs(file_path: str) -> str:
    """Upload to ipfs

    Args:
        nft_path (str): path to metadata file
    """
    with open(file_path, "rb") as f:
        nft_binary = f.read()
    ipfs_endpoint = "http://127.0.0.1:5001/"
    api = "api/v0/add"
    nft_name = file_path.split("/")[-1:][0]
    ipfs_hash = requests.post(ipfs_endpoint + api, files={"from": nft_binary}).json()[
        "Hash"
    ]
    nft_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={nft_name}"
    print("IPFS address: ", nft_uri)
    return nft_uri


def set_uri(nft, uri: str, nft_id: int = 0):
    """Call the setTokenURI function of the NFT contract
    and set the URI for the NFT id.

    Args:
        uri (str): metadata link
        nft_id (int): nft id
    """
    acc = get_account()
    print('Account balance: ', acc.balance())
    # acc.transfer(nft.address, '0.1 ether')
    # print('Account balance: ', acc.balance())
    acc = get_account()
    tx = nft.createNFT({"from": acc})
    tx.wait(1)
    if nft_id == 0:
        nft_id = nft.tokenCount()
        ic(nft.id2sender(nft_id))
        ic(nft.getSender({'from': acc}))
        ic(nft.getCurrentNumber())
        print("NFT token id set to: {}".format(nft_id))

    tx2 = nft.setTokenURI(nft_id, uri, {"from": acc})
    tx2.wait(1)
    opensea_url = "https://testnets.opensea.io/{}".format(nft.address)
    print("You can now find your NFT on: \n{}\n".format(opensea_url))

    return opensea_url


def main():
    """Main app to upload NFT to ipfs."""
    if network.show_active() in LOCAL_BLOCKCHAINS:
        nft = deploy_adv_nft()
    else:
        nft = AdvancedNFT[-1]
    img_path = "./res/img/goku-2019.png"
    img_url = upload2ipfs(img_path)
    meta_path = create_meta(img_url)
    meta_url = upload2ipfs(meta_path)
    set_uri(nft, meta_url)
