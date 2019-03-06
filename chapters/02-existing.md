# Existing solutions

## Blockchain	

DLT[^1] allows us to have a single data silo (albeit specialized) that is spread across all users of the network. Smart-Contracts make use of that ability to allow decentralized computing (among other benefits).

Common naming of dApps[^2] is using smart contracts on blockchain platforms like Ethereum. A few issues arise from its model:

- Paid transactions by the user (meaning a dApp user should buy some underlying network asset to use the Dapp)
- Reliance on inclusion in a block (dependant on the block time of the relevant blockchain, making dApps slow)
- On-chain storage is very expensive, making it unsuitable for media content or large documents.

There are a lot of existing blockchain platforms currently active [see @coinmarketcap].

\clearpage

## DHT storages like IPFS

Storage networks like IPFS or Swarm are great to find a resource based on its hash in the network.
Some things are currently needed or not easily useable for our dApps:

- Incentivization of storage (to be implemented in their FileCoin for IPFS, implemented on Ethereum for Swarm)
- Unique resource naming system (provided in a slow way currently by IPNS, fix being worked on, or through Ethereum smart contracts in Swarm)

```{.mermaid caption="Typical smart-contract based dApp using IPFS"}
graph LR
  User(User) --- Frontend(Frontend)
  Frontend --- APIS(API Server)
  APIS --- SmartContract
  APIS --- BlockChain
  SmartContract --- BlockChain
  Frontend --- IPFS("IPFS<br>(dApp data pinned<br>by dApp owner)")
  
  class User,Frontend,APIS,SmartContract,IPFS,BlockChain icon-node;
  class User boy;
  class Frontend web;
  class APIS api;
  class SmartContract contract;
  class IPFS ipfs;
  class BlockChain blockchain;
```




[^1]: Distributed Ledger Technology, mostly BlockChain
[^2]: Decentralized applications

