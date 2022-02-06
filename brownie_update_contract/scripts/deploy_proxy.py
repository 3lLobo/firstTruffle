from brownie import (
    Contract,
    network,
    Box,
    BoxV2,
    ProxyAdmin,
    TransparentUpgradeableProxy,
)
from scripts.utils import get_account, encode_function_data, upgrade_contract


def deploy_box(set_val):
    """Deploy Box contract."""
    acc = get_account()
    print("Deploying to {}".format(network.show_active()))
    box = Box.deploy({"from": acc})

    proxy_admin = ProxyAdmin.deploy({"from": acc})
    # initializer = box.store, 1
    box_init_bytes = encode_function_data()

    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        box_init_bytes,
        {"from": acc, "gas_limit": 1e6},
    )
    print("Deployed TransparentUpgradeableProxy to {}".format(proxy.address))
    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)
    tx = proxy_box.store(set_val, {"from": acc})
    tx.wait(1)
    print('Deployed value through proxy is:  ', proxy_box.retrieve())

    return proxy_admin, proxy


def main():
    """Main app."""
    deploy_box(11)
