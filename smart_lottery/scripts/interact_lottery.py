"""Script to interact with the blockchain
"""

import time
from brownie import Lottery
from scripts.deploy import deploy_lot
from scripts.utils import fund_link, get_account, get_contract
from icecream import ic


def start_lot():
    """Start the Lottery."""
    acc = get_account()
    lot = Lottery[-1]
    tx_start = lot.startLottery({"from": acc})
    tx_start.wait(1)
    print("Lottery started!")


def b_victim(idx: int = 0):
    """Enter the Lottery.

    Args:
        idx (int, optional): Account index to join. Defaults to 0.
    """
    acc = get_account(acc_idx=idx)
    lot = Lottery[-1]
    fee = lot.getEntranceFee() + 111
    lot.enter({"from": acc, "value": fee})
    print("You are in!")


def end_lot():
    """End the lottery and draw winner.
    """
    acc = get_account()
    lot = Lottery[-1]
    tx = fund_link(lot)
    tx.wait(1)
    tx_end = lot.endLottery({"from": acc})
    tx_end.wait(1)
    time.sleep(11)
    print(f"Player {lot.recentWinner()} won the Lottery!")


def main():
    """Main app to interact with Lottery contract."""
    deploy_lot()
    start_lot()
    # for n in range(6):
    b_victim()
    end_lot()
