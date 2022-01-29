"""Test the VRF randomness.
"""

from scripts.advanced.deploy_adv_nft import deploy_adv_nft
from scripts.utils import fund_link, get_account, get_contract
from brownie import AdvancedNFT


def test_advanced_nft():
    """Test the randomness of the VRF
    """
    # Arrange
    acc = get_account()
    # Act
    nft, tx = deploy_adv_nft('test_uri.json')
    req_id = tx.events['requestedCollectable']['requestId']

    # Assert
    assert nft.tokenCount() == 1
    assert nft.requestId2Sender(req_id) == acc

    rdm_n = 111
    vrf = get_contract('vrf')
    assert vrf.callBackWithRandomness(req_id, rdm_n, acc)
    # tx2 = nft.fulfillRandomness(req_id, rdm_n)
    assert nft.id2goku(nft.tokenCount()) == rdm_n % 3    


