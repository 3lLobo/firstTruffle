// "SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract AdvancedNFT is ERC721, VRFConsumerBase {
    Counters.Counter public tokenCount;
    bytes32 public keyhash;
    uint256 public fee;
    enum Goku {
        G2019,
        G2020,
        G2021
    }
    mapping(uint256 => Goku) public id2goku;
    mapping(bytes32 => address) public requestId2Sender;
    event requestedCollectable(bytes32 indexed requestId, address requester);

    constructor(
        address _vrf,
        address _link,
        bytes32 _keyhash,
        uint256 _fee
    ) VRFConsumerBase(_vrf, _link) ERC721("Goku", "GOK") {
        Counters.reset(tokenCount);
        keyhash = _keyhash;
        fee = _fee;
    }

    function createNFT(string memory _uri) public returns (bytes32) {
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestId2Sender[requestId] = msg.sender;
        Counters.increment(tokenCount);
        emit requestedCollectable(requestId, msg.sender);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber)
        internal
        override
    {
        Goku goku = Goku(randomNumber % 3);
        uint256 newId = Counters.current(tokenCount);
        id2goku[newId] = goku;
        address owner = requestId2Sender[requestId];
        _mint(owner, newId);
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "U R not the Owwwnerrr!"
        );
        setTokenURI(tokenId, _tokenURI);

    }

}
