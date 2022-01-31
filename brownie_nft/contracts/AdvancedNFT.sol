// "SPDX-License-Identifier: UNLICENSED

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract AdvancedNFT is ERC721URIStorage, VRFConsumerBase {
    Counters.Counter public tokenCount;
    bytes32 public keyhash;
    uint256 public fee;
    enum Goku {
        G2019,
        G2020,
        G2021
    }
    mapping(uint256 => Goku) public id2goku;
    mapping(uint256 => address) public id2sender;
    mapping(bytes32 => address) public requestId2Sender;

    // mapping(uint256 => address) public _owners;

    // function getOwnerr(uint256 _id) public view returns(address) {
    //     return _owners[_id];
    // }

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

    function createNFT() public returns (bytes32) {
        Counters.increment(tokenCount);
        id2sender[Counters.current(tokenCount)] = msg.sender;
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestId2Sender[requestId] = msg.sender;
        emit requestedCollectable(requestId, msg.sender);
        return requestId;
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber)
        internal
        override
    {
        Goku goku = Goku(randomNumber % 3);
        uint256 newId = Counters.current(tokenCount);
        address nft_owner = id2sender[newId];
        id2goku[newId] = goku;
        _safeMint(nft_owner, newId);
    }

    function getCurrentNumber() public view returns(uint256) {
        return Counters.current(tokenCount);        
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {
        require(
            _isApprovedOrOwner(_msgSender(), tokenId),
            "U R not the Owwwnerrr!"
        );
        _setTokenURI(tokenId, _tokenURI);
    }

    function getSender() public view returns(address) {
        return _msgSender();        
    }

    function nft_exits(uint256 nft_id) public view returns (uint256) {
        if (_exists(nft_id)) {
            return 1;
        } else {
            return 0;
        }
    }
}
