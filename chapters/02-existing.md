# Existing solutions

## Blockchain	

DLT[^1] allows to have a single data silo (albeit specialized) that is spread accross all users of the network. Smart-Contracts make use of that ability to allow decentralized computing (among other benefits).

Common naming of dApps[^2] is using smart contracts on blockchain platforms like Ethereum. A few issues arise from its model:

- Paid transactions by the user (meaning a dApp user should buy some underlying network asset to use the Dapp)
- Reliance on inclusion in a block (dependant on block time of the relevant blockchain, making dApps slow)

There is a lot of existing blockchain platforms currently active [see @coinmarketcap].

## DHT storages like IPFS

Storage networks like IPFS or Swarm are great to find a resource based on its hash in the network.
Some things are currently needed or not easily useable for our dApps:

- Incentivization of storage (to be implemented in their FileCoin for IPFS, implemented on ethereum for Swarm)
- Unique resource naming system (provided in a very slow way currently by IPNS, or through Ethereum smart contracts in Swarm)




[^1]: Distributed Ledger Technology, mostly BlockChain
[^2]: Decentralized applications

