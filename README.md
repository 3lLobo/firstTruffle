
# My First Truffle

A collection of projects as I learn how to write smart contract and interact with the ETH blocqchain.


## Badges

Here some badges:

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?style=for-the-badge)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)


![GitHub language count](https://img.shields.io/github/languages/count/3lLobo/firstTruffle?style=for-the-badge)


![GitHub top language](https://img.shields.io/github/languages/top/3lLobo/firstTruffle?style=for-the-badge)


![GitHub commit activity](https://img.shields.io/github/commit-activity/y/3lLobo/firstTruffle?color=lightblue&style=for-the-badge)


![Lines of code](https://img.shields.io/tokei/lines/github/3lLobo/firstTruffle?style=for-the-badge)


## Authors

- [@3lLobo](https://www.github.com/3lLobo)


## Lessons Learned

Useful blocqchain links:
 - [Tutorial repo](https://github.com/smartcontractkit/full-blockchain-solidity-course-py)
 - [ETH blovkchain explorer](https://etherscan.io/)
 - [Rigby testnet explorer](https://rinkeby.etherscan.io/)
 - [Gas indicator](https://ethgasstation.info/)
 - [Browser IDE](https://remix.ethereum.org/)
 - [request fake moneyyy - Rinkeby Ether](https://docs.chain.link/docs/link-token-contracts/#rinkeby)

On remix, choose __injected Web3__ and Meta will pop up.

One Wei is the smallest breakdown of ether, can't go smaller than Wei.

### in Solidity

To get data, a contract address has to be provided. To get the current eth price, call the contract address provided by [chainlink](https://data.chain.link/ethereum/mainnet/crypto-usd).

__this__ returns the contracts own address. Calling adress.balance retruns the accounts funds in wei. Constructor( is called when the contract is deployed, similar to init().

__modifier__ can be used to condition functions. Needs _; as last line.

### in Python
 
```python
solcx.compile_standard
```
This will compile the provided __.sol__ file and return the logs.


 - contract requires: abi, bytecode
 - build Transaction requires: contract, chainId, address, nonce, gassPrice
 - sign Transaction requires: transaction, privateKey
 - -> then: send_raw_transaction
 - wait for transaction receipt return the transaction information, most important the contract address

Alternative: use brownie. 
```
pip install eth-brownie
```
Then init the project by cd-ing into the parent folder and call brownie init.
store your solidity contracts in contracts folder and run 

```
brownie compile
```

Next write your python app in scripts and run them with 
```
brownie run scripts/{}.py --network {}
```
Choose which network to interact with. By default brownie launches a ganache dev chain.
Store env Variables in a .env file then create a __brownie-config.yaml__ file and add ```dotenv: .env```. 
A custom wallet can be added to brownie with ```brownie accounts new {name}``` or in the yaml file:

```
wallets:
  from_key: ${PRIV_KEY}
```

To deloy contracts on non-local blockchains, we need to specify ``` WEB3_INFURA_PROJECT_ID```. A project can be created on [Infura](https://infura.io/) and the project ID save in the __.env__ file.



### Ganache

To install ganache cli do the following:
 - install nodejs
 - install npm
 - npm install --global yarn
 - yarn global add ganache-cli
 - ganache-cli --deterministic for always the same addresses

Ganache hides between a bunch of other frameworks. Think ```global``` avoids it installing only for the current project.

<!-- .markdown-body {
  --md-code-background: #e3dcef;
  --md-code-text: #4a2b7b;
  --md-code-tabs: #c6b8dd;
  --md-code-radius: 4px;
} -->

## Running Tests

For the brownie project, which is the only one with test so far. Place the tests in the test subfolder and run:
```bash
  brownie test
```
brownie test is based on pytest and accepts the very same arguments. Add ```-Pdb``` to launch the debuger on crash.

__I'm hangrey now!__

## Appendix

Any additional information goes here


## License

[MIT](https://choosealicense.com/licenses/mit/)


