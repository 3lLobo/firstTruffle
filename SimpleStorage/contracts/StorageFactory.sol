// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./SimpleStorage.sol";

contract StorageFactory is SimpleStorage {

    SimpleStorage[] public simpleStorageArray;

    function createSScontract() public {
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorageArray.push(simpleStorage);
        
    }

    function storeSF(uint256 _sSindex, string memory _sSname) public {
        // Adress
        // ABI
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_sSindex]));
        simpleStorage.store2(_sSname);

    }

    function getSF(uint256 _favNumber) public view returns (string memory) {
        SimpleStorage simpleStorage = SimpleStorage(address(simpleStorageArray[_favNumber]));
        return simpleStorage.retrieve();
    }
}
