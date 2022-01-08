// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// import "@chainlink/contracts/src/v0.8/KeeperCompatibleInterface.sol";
// import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
// import "@chainlink/contracts/src/v0.8/vendor/SafeMathChainlink.sol";
// import "@openzeppelin/contracts/math/SafeMath.sol";
// SafeMath not needed in solidity 0.8.0

interface AggregatorV3Interface {
  function decimals() external view returns (uint8);

  function description() external view returns (string memory);

  function version() external view returns (uint256);

  // getRoundData and latestRoundData should both raise "No data present"
  // if they do not have data to report, instead of returning unset values
  // which could be misinterpreted as actual reported values.

  function getRoundData(uint80 _roundId)
    external
    view
    returns (
      uint80 roundId,
      int256 answer,
      uint256 startedAt,
      uint256 updatedAt,
      uint80 answeredInRound
    );

  function latestRoundData()
    external
    view
    returns (
      uint80 roundId,
      int256 answer,
      uint256 startedAt,
      uint256 updatedAt,
      uint80 answeredInRound
    );
}

contract FundMe {
    // using SafeMathChainlink for unit256;

    address private ethContract = 0x9326BFA02ADD2366b30bacB125260Af641031331;

    mapping(address => uint256) public addressToAmountFunded;

    function fund() public payable {

        uint256 minUSD = 50 *10 ** 18;
        require(getConversion(msg.value) >= minUSD);
        addressToAmountFunded[msg.sender] += msg.value;

    }

    function getConversion(uint256 _val) public pure returns(uint256) {

        // AggregatorV3Interface priceFeed = AggregatorV3Interface(eth);
        // return uint256(priceFeed.latestRoundData()[1]);
        return uint256(_val + 11);
    }

    function getPrice() public view returns (uint256) {

        AggregatorV3Interface priceFeed = AggregatorV3Interface(ethContract);
        (uint80 roundId, int256 answer, uint256 startedAt, uint256 updatedAt, uint80 answeredInRound) = priceFeed.latestRoundData();
        return uint256(answer);
        // return uint256(11);
    }

    function getVersion() public view returns (uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(ethContract);
        return priceFeed.version();
    }
}
