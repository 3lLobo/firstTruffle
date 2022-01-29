// SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract SimpleNFT is ERC721 {
    uint256 public tokenCount;

    constructor() public ERC721("Dawhg", "DOGE") {
        tokenCount = 0;
    }

    function createNFT(string memory tokenURI) public returns (uint256) {
        uint256 newTokenId = tokenCount;
        _mint(msg.sender, newTokenId);
        tokenCount += 1;
        return newTokenId;
    }

    // function mintNFT(type name) {

    // }
}
