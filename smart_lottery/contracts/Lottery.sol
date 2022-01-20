// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract Lottery {
    address[] public victims;
    uint256 public usdFee;
    AggregatorV3Interface internal priceFeed;

    constructor(address _feedAddress) {
        usdFee = 50 * (10**18);
        priceFeed = AggregatorV3Interface(_feedAddress);
    }

    function enter() public payable {
        // Enter the lottery
        require(msg.value >= usdFee);
        victims.push(msg.sender);
    }

    function getEntranceFee() public view returns (uint256) {
        // return the entracnce fee
        int256 price = getEthPrice();
        uint256 newprice = uint256(price) * 10**10; // 18 Decimals
        uint256 priceEth = (usdFee * 10**18) / newprice;
        return priceEth;
    }

    function startLottery() public {
        // Start the Lottery
    }

    function endLottery() public {
        // End lottery and chose winner
    }

    function getEthPrice() public view returns (int256) {
        // Get and return the current Eth price in Usd.
        (, int256 price, , , ) = priceFeed.latestRoundData();
        return price;
        // return price;
    }
}
