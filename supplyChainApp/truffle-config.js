const HDWalletProvider = require("@truffle/hdwallet-provider");
var mnemonic = "0x3ECC53F7Ba45508483379bd76989A3003E6cbf09";

module.exports = {
  networks: {
   development: {
    host: "127.0.0.1",
    port: 8545,
    network_id: "*"
   },
   ropsten: {
       provider: function() { 
        return new HDWalletProvider(mnemonic, "https://ropsten.infura.io/v3/db7278945d1741a4963fdcaa6a0c47e6");
       },
       network_id: 3,
       gas: 4500000,
       gasPrice: 10000000000,
   },
   live: {
    provider: function() { 
     return new HDWalletProvider(mnemonic, "https://mainnet.infura.io/v3/db7278945d1741a4963fdcaa6a0c47e6");
    },
    network_id: 1,
    gas: 7500000,
    gasPrice: 10000000000,
}
  }
 };
