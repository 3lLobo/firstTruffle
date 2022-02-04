from brownie import (
    Contract,
    network,
    Box,
    BoxV2,
    ProxyAdmin,
    TransparentUpgradeableProxy,
)
from scripts.utils import get_account, encode_function_data


def deploy_box():
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
    tx = proxy_box.store(11, {"from": acc})
    tx.wait(1)
    print('Deployed value through proxy is:  ', proxy_box.retrieve())


def main():
    """Main app."""
    deploy_box()
