// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;

contract SimpleStorage {

    // store some data
    bytes32 myName = "3lLobo";
    string myName2;

    function i_store(bytes32 _myBytes) public {
        myName = _myBytes;

    }

    function store2(string memory _name) public {
        myName2 = _name;

    }

    function retrieve() public view returns(string memory) {
        return myName2;        
    }

    function retrieve_view() public view returns(bytes32) {
        return myName;

    }

    function retrive_view(bytes32 _myBytes) public pure returns(bytes32) {
        return _myBytes;

    }

    struct Ship {
        uint256 ship_years;
        string friend_ship_name;
    }

    Ship public silVisser = Ship({ship_years: 3, friend_ship_name: "Sil"});

    Ship[] public myFriends;

    mapping(string => uint256) public name2number;

    // strings akways need memory or if it should persist, stoarge
    function addFriend(string memory _name, uint32 _years) public {

        myFriends.push(Ship({ship_years: _years, friend_ship_name: _name}));
        name2number[_name] = _years;
        
    }

}