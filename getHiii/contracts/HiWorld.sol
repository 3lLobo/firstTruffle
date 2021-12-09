// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

contract HiWorld {

    function checkOwner(string calldata caller) private view returns (bool) {
        require(msg.sender == caller);
        revert();
        assert(msg.sender == caller);
    }

    

    string private hiii = "Hi strijder!";

    function getHiii() public view returns (string memory) {
        return hiii;
    }
}