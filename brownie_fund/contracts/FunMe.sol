// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/KeeperCompatibleInterface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";


contract FundMe {
    // using SafeMathChainlink for unit256;

    address private ethContract = 0x9326BFA02ADD2366b30bacB125260Af641031331;

    mapping(address => uint256) public addressToAmountFunded;

    address private owner;
    address[] public funders;

    constructor() {
        owner = msg.sender;
    }

    function fund() public payable {
        uint256 minUSD = 50 * 10**18;
        require(getConversion(msg.value) >= minUSD, "Send more!");
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

    function getConversion(uint256 _val) public view returns (uint256) {
        uint256 ethPrice = getPrice();
        return wei2usd((_val * ethPrice) / 10e10);
    }

    function wei2usd(uint256 _val) public pure returns (uint256) {
        return _val / 10e18;
    }

    function getPrice() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(ethContract);
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
        AggregatorV3Interface priceFeed = AggregatorV3Interface(ethContract);
        return priceFeed.version();
    }

    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }
}
