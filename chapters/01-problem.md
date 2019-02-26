# Problem (existing state of the industry)

Internet has been built to connect computer together. It has been used as a marvelous communication and data storage model. Our protocols originally designed for decentralization are showing their limits.

In a purely economy driven world, simplicity, centralization and non-standard data models tends to win.

What is our internet today? Silos loosely connected together, users having data in each of those silos (Facebook, Google, and many others), with no simple way to port it over.

There is a lot of attempts at breaking those silos, from connection from silo to silo (iftt, rgpd for data request, opendata programs...), to decentralized networks of silos (mastodon). We are living in a world of data silos.

In itself, it isn't bad. If those silos were easily accessible, and decentralized. Users don't know it, but they need to reclaim their data.

## Blockchain	

DLT[^1] allows to have a single data silo (albeit specialized) that is spread accross all users of the network. Smart-Contracts make use of that ability to allow decentralized computing (among other benefits).

Common naming of dApps[^2] is using smart contracts on blockchain platforms like Ethereum. A few issues arise from its model:

- Paid transactions by the user (meaning a dApp user should buy some underlying network asset to use the Dapp)
- Reliance on inclusion in a block (dependant on block time of the relevant blockchain, making dApps slow)

## DHT storages like IPFS

Storage networks like IPFS or Swarm are great to find a resource based on its hash in the network.
Some things are currently needed or not easily useable for our dApps:
- Incentivization of storage (to be implemented in their FileCoin for IPFS, implemented on ethereum for Swarm)
- Unique resource naming system (provided in a very slow way currently by IPNS, or through Ethereum smart contracts in Swarm)




[^1]: Distributed Ledger Technology, mostly BlockChain
[^2]: Decentralized applications
