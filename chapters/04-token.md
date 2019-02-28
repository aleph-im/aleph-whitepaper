# Aleph Token

## Rewards

Two main sources of reward and token creation are:

- Reward each signed message written to underlying blockchain.
- Reward storage of application data (pin items) and availability of API, both are mandatory for nodes.

Of those rewards, a part will come from monetary creation, and a part from dApp owner incentive to prioritize their apps and their user fees.

If a dApp owner wants to get the benefit of the network without having to rely on third parties only, he can run a node of the network where he prioritize his dApp data (but can't ignore completely others, having a backup for his users on other nodes, while he gives the same allowance to other dApps).

## Token use

Most node owners will accept free storage of dApp data, especially at start of the network. Once the data grows bigger, and having all the data on all the hosts starts being impractical, dApp owners can pay for storage and writes to blockchain of his dApp data.

Alternatively, application users can pay themselves for the storage of their data (example, big data volume like picture storage applications).

## Token details

The first issuance of the Aleph utility token will be made as an NRC-20 token, which will be able to be swapped for the native asset at a later date.

If technically possible, the switch between nrc-20 and native aleph token will be available in both directions.

## Initial token distribution

Exact details will be announced later on, here is the planned token distribution (can be subject to changes).

To reward the NULS community and ecosystem, a big part of the supply will be airdropped to NULS token holders.

1,000,000,000 (1 billion) tokens will be issued initially.

Of those :

  - 400M will be airdropped (most likely to NULS token holders, details will be anounced through official channels),
  - 600M to the Aleph team (who might be able to sell some in OTC trades for development funding and/or allocate a part for a community or foundation fund)

```{.python .run caption="Token Distribution" label="my_fig" hide_code=True}
import matplotlib
matplotlib.use('AGG')
from matplotlib import pyplot as plt

# create data
names='Airdrop\n400M', 'Aleph Team\n600M',
size=[400,600]
 
# Create a circle for the center of the plot
my_circle=plt.Circle( (0,0), 0.7, color='white')
plt.pie(size, labels=names, wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' })
p=plt.gcf()
p.gca().add_artist(my_circle)
```

## Supply evolution

Through the described rewards the token supply will approximately grow by 10% the first year, then the inflation rate will decrease by 2% each year until it reaches 4% per year and stays at that value.

|                |1st year|2nd year|3rd year|4th year|5th year|6th year|
|---------------:|-------:|-------:|-------:|-------:|-------:|-------:|
|       inflation|     10%|      8%|      6%|      4%|      4%|      4%|
|   tokens minted|    100M|     88M|  71.28M|  50.37M|  52.38M|  54.48M|
|total supply eoy|   1100M|   1188M|   1259M|   1309M|   1362M|   1416M|

While the part devoted to the team and developement may seem high on issuance, the inflation rate makes it lower than the rest of the circulating supply during the 3rd year.





