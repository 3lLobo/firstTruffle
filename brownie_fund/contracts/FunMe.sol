// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/KeeperCompatibleInterface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

// import "@chainlink-mix/contracts/test/MockV3Aggregator.sol";

contract FundMe {
    // using SafeMathChainlink for unit256;

    // address private ethContract = 0x9326BFA02ADD2366b30bacB125260Af641031331;

    mapping(address => uint256) public addressToAmountFunded;

    address private owner;
    address[] public funders;
    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) {
        owner = msg.sender;
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    function getEntranceFee() public view returns (uint256) {
        // minimum fee in USD
        uint256 minUSD = 50 * 10**18;
        uint256 price = getPrice();
        uint256 precision = 1 * 10**18;
        return (minUSD * precision) / price;
    }

    function fund() public payable {
        uint256 minUSD = 50 * 10**18;
        require(
            getConversionRate(msg.value) >= minUSD,
            "You need to spend more ETH!"
        );
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    function withdraw() public payable {
        require(msg.sender == owner);
        payable(msg.sender).transfer(address(this).balance);
        for (uint256 fi = 0; fi < funders.length; fi++) {
            address funder = funders[fi];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }

    function getConversionRate(uint256 ethAmount)
        public
        view
        returns (uint256)
    {
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        // the actual ETH/USD conversation rate, after adjusting the extra 0s.
        return ethAmountInUsd;
    }

    function wei2usd(uint256 _val) public pure returns (uint256) {
        return _val / 10000000000;
    }

    function getPrice() public view returns (uint256) {
        (
            uint80 roundId,
            int256 answer,
            uint256 startedAt,
            uint256 updatedAt,
            uint80 answeredInRound
        ) = priceFeed.latestRoundData();
        return uint256(answer * 10e10);
        // return uint256(11);
    }

    function getVersion() public view returns (uint256) {
        return priceFeed.version();
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }
}
