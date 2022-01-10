// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract HiWorld {
    address public owner = msg.sender;

    function checkOwner() private view returns (bool) {
        require(msg.sender == owner);
        // revert();
        assert(msg.sender == owner);
        return true;
    }

    string private hiii = "Hi strijder!";

    function getHiii() public view returns (string memory) {
        return hiii;
    }
}
