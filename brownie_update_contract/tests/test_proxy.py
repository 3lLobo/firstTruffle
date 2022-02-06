"""Test the proxy-contract
"""


from brownie import exceptions, BoxV2, Contract
import pytest
from scripts.deploy_proxy import deploy_box
from scripts.utils import upgrade_contract, get_account


def test_TestProxy():
    """Test the whole class"""
    tp = TestProxy("tp")
    tp.test_deploy_proxy()
    tp.test_admin()
    tp.test_upgrade()


class TestProxy():
    def __init__(
        self,
        name: str,
        parent: "Optional[Node]" = None,
        config: "Optional[Config]" = None,
        session: "Optional[Session]" = None,
        fspath: "Optional[py.path.local]" = None,
        nodeid: "Optional[str]" = None,
    ) -> None:
        super().__init__()

        self.set_value = 11
        proxy_admin, proxy_contract = deploy_box(self.set_value)
        self.proxy_admin = proxy_admin
        self.proxy_contract = proxy_contract
        self.acc = get_account()

    def test_deploy_proxy(
        self,
    ):
        """Test if the contract is deployed correctly."""
        assert self.acc.address != self.proxy_admin.address
        assert self.proxy_admin.getProxyAdmin(self.proxy_contract, {"from": self.acc}) == self.proxy_admin.address

    def test_admin(self):
        """Test if the admin address is used."""
        with pytest.raises(exceptions.VirtualMachineError):
            self.proxy_contract.admin()

    def test_upgrade(self):
        """Test if contract can be upgraded."""
        boxv2 = BoxV2.deploy({"from": self.acc})
        tx = upgrade_contract(self.acc, self.proxy_contract, boxv2.address, self.proxy_admin)

        proxy_boxv2 = Contract.from_abi("BoxV2", self.proxy_contract.address, BoxV2.abi)

        assert proxy_boxv2.retrieve() == self.set_value
        proxy_boxv2.increment({"from": self.acc})
        assert proxy_boxv2.retrieve() == self.set_value + 1
