"""Mint wether by borrowing eth.
"""


from idna import valid_contextj
from scripts.utils import get_account
from brownie import interface, network, config
from web3 import Web3

def get_weth():
    """get weth function
    """
    acc = get_account()
    print("ETH balance: ", Web3.fromWei(acc.balance(), 'ether'))
    weth = interface.WethInterface(config['networks'][network.show_active()]['weth_token'])
    txx = weth.deposit({'from': acc, 'value': acc.balance()/2})
    print('Recieved weth')
    return txx




def main():
    get_weth()
