from brownie import SimpleStorage, accounts


def test_deploy():
    """testing steps:
    1. Arrange
    2. Act
    3. Assert
    """
    acc = accounts[0]
    ss_contract = SimpleStorage.deploy({"from": acc})
    start_val = ss_contract.retrieve()
    expected = "3lLobo"

    assert start_val == expected


def test_store():
    """test the storing function
    SimpleStorage -> store2
    """
    # Arrange
    acc = accounts[0]
    ss_contract = SimpleStorage.deploy({"from": acc})

    # Act
    expect = '11'
    ss_contract.store2(expect, {'from': acc})
    assert ss_contract.retrieve() == expect