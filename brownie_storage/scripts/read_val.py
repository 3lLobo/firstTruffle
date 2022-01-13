"""Read stuff off the blocqchain
"""

from brownie import SimpleStorage, accounts, config
from icecream import ic
from scripts.brownie_deploy import get_account


def read_contract():
    """reads the contact address."""
    ss_contract = SimpleStorage[-1]
    ic(ss_contract.retrieve())


def read_mate(name) -> int:
    """Reads the names of the sould on your FriendShip.

    Args:
        name ([str]): the name of your mate

    Returns:
        int: years you've been friends
    """
    ss_contract = SimpleStorage[-1]
    acc = get_account()
    n = 0
    while True:
        n += 1
        try:
            friends = ss_contract.myFriends(n, {'from': acc})
            ic(friends)
        except:
            break

    sil = ss_contract.silVisser({'from': acc})
    ic(sil)

    return ss_contract.name2number(name)



def main():
    read_contract()
    mate = 'Nuka <3'
    print("You and {} have been mates for {} years!".format(mate, read_mate(mate)))
