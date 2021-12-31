#!bin/bash

cd getHiii
truffle console; HiWorld.deployed().then(function(beep) {return beep.getHiii()};) 