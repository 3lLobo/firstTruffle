// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract Lottery is VRFConsumerBase, Ownable {
    address[] public victims;
    address payable public recentWinner;
    uint256 public usdFee;
    uint256 public randomness;
    AggregatorV3Interface internal priceFeed;
    event RequestedRandomness(bytes32 requestId);

    enum LOT_STATE {
        CLOSED,
        OPEN,
        CALC
    }

    LOT_STATE public lot_state;
    uint256 public fee;
    bytes32 public keyHash;

    constructor (
        address _feedAddress,
        address _vrfFeed,
        address _link,
        uint256 _fee,
        bytes32 _keyHash
    ) public VRFConsumerBase(_vrfFeed, _link) {
        usdFee = 50 * (10**18);
        priceFeed = AggregatorV3Interface(_feedAddress);
        lot_state = LOT_STATE.CLOSED;
        fee = _fee;
        keyHash = _keyHash;
    }

    function enter() public payable {
        // Enter the lottery
        require(lot_state == LOT_STATE.OPEN);
        require(msg.value >= getEntranceFee());
        victims.push(msg.sender);
    }

    function getEntranceFee() public view returns (uint256) {
        // return the entracnce fee
        int256 price = getEthPrice();
        uint256 newprice = uint256(price) * 10**10; // 18 Decimals
        uint256 priceEth = (usdFee * 10**18) / newprice;
        return priceEth;
    }

    function startLottery() public onlyOwner {
        // Start the Lottery
        require(lot_state == LOT_STATE.CLOSED);
        lot_state = LOT_STATE.OPEN;
    }

    function endLottery() public onlyOwner {
        // End lottery and chose winner
        // TODO Random
        // pseudo_rand = uint256(keccak256(abi.encodePacked(nonce, msg.sender, block.difficulty, block.timestamp ))) % victims.lenght;
        lot_state = LOT_STATE.CALC;
        bytes32 requestId = requestRandomness(keyHash, fee);
        emit RequestedRandomness(requestId);
    }

    function fulfillRandomness(bytes32 _requestId, uint256 _randomness)
        internal
        override
    {
        require(lot_state == LOT_STATE.CALC);
        require(_randomness > 0);
        require(victims.length > 0);
        uint256 idxWinner = _randomness % victims.length;
        recentWinner = payable(victims[idxWinner]);
        recentWinner.transfer(address(this).balance);
        // reset
        victims = new address[](0);
        randomness = _randomness;
        lot_state = LOT_STATE.CLOSED;
    }

    // function fulfillRandomness(bytes32 _requestId, uint256 _randomness)
    //     internal
    //     override
    // {
    //     require(lot_state == LOT_STATE.CALC);
    //     require(_randomness > 0);
    // }

    function getEthPrice() public view returns (int256) {
        // Get and return the current Eth price in Usd.
        (, int256 price, , , ) = priceFeed.latestRoundData();
        return price;
        // return price;
    }
}
