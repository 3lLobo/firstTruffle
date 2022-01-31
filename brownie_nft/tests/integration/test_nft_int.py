"""Integration test for deploying NFT. On chain.
"""

import pytest
from scripts.advanced.deploy_adv_nft import deploy_adv_nft
from scripts.utils import LOCAL_BLOCKCHAINS, fund_link, get_account, get_contract
from brownie import AdvancedNFT, network


def test_advanced_nft():
    """Test the randomness of the VRF
    """
    if network.show_active() in LOCAL_BLOCKCHAINS:
        pytest.skip("Test on chain!")
    # Arrange
    acc = get_account()
    # Act
    nft, tx = deploy_adv_nft('test_uri.json')
    req_id = tx.events['requestedCollectable']['requestId']

    # Assert
    assert nft.tokenCount() == 1
    assert nft.requestId2Sender(req_id) == acc