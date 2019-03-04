# Aleph Token

## Rewards

Three main sources of reward and token creation are:

- Reward each signed message written to underlying blockchain.
- Reward storage of application data (pin items) and availability of API, both are mandatory for nodes.
- POCM NULS token locking in NULS underlying chain (see token distribution secion)

Of those rewards, a part will come from monetary creation, and a part from dApp owner incentive to prioritize their apps and their user fees.

If a dApp owner wants to get the benefit of the network without having to rely on third parties only, he can run a node of the network where he prioritize his dApp data (but can't ignore completely others, having a backup for his users on other nodes, while he gives the same allowance to other dApps).

## Token use

Most node owners will accept free storage of dApp data, especially at start of the network. Once the data grows bigger, and having all the data on all the hosts starts being impractical, dApp owners can pay for storage and writes to blockchain of his dApp data.

Alternatively, application users can pay themselves for the storage of their data (example, big data volume like picture storage applications).

## Token details

The first issuance of the Aleph utility token will be made as an NRC-20 token first, which will be able to be swapped for the native asset at a later date.

If technically possible (part under research):

- the switch between nrc-20 and native aleph token will be available in both directions.
- the token will also be made available as an erc-20 token

## Initial token distribution

Exact details will be announced later on, here is the planned token distribution (can be subject to changes).

To reward the NULS community and ecosystem, a big part of the supply will be airdropped to NULS token holders.

1,000,000,000 (1 billion) tokens will be issued initially.

Of those :

  - 150M will be airdropped (most likely to NULS token holders, details will be anounced through official channels),
  - 250M will be reserved for an extra incentive on POCM mining program
  - 600M to the Aleph team (who will use this for bootstrap period rewards, might be able to sell some for development funding, allocate a part for a community or foundation fund or any other use it might deem necessary)

```{.python .run caption="Token Distribution" label="allocation_fig" hide_code=True}
import matplotlib
matplotlib.use('AGG')
# import seaborn as sns
from matplotlib import pyplot as plt

plt.figure()

#plt.style.use('seaborn-paper')

# create data
names='Airdrop\n150M', 'POCM\n250M', 'Reserved\n600M',
size=[150,250,600]
 
# Create a circle for the center of the plot
my_circle=plt.Circle( (0,0), 0.7, color='white')
plt.pie(size, labels=names, wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' })
p=plt.gcf()
p.gca().add_artist(my_circle)
```

### NULS staking program (POCM)

In addition to a regular airdrop, NULS holders can lock a part of their NULS tokens to get Aleph tokens.

While their tokens are locked, they will receive Aleph tokens based on the NULS amount they "staked"/"locked".

Those tokens will come from an initial pool of 250M tokens, locked for that purpose. Once that pool dries up (after approximately 2-3 years), the reward will be lowered and the tokens minted using this program will be taken from the Supply Evolution.

## Supply evolution

Once the full network is ready (see roadmap chapter) and through the described rewards the token supply will approximately grow by 10% the first year, then the inflation rate will decrease by 2% each year until it reaches 4% per year and stays at that value.

|                |1st year|2nd year|3rd year|4th year|5th year|6th year|
|---------------:|-------:|-------:|-------:|-------:|-------:|-------:|
|       inflation|     10%|      8%|      6%|      4%|      4%|      4%|
|   tokens minted|    100M|     88M|  71.28M|  50.37M|  52.38M|  54.48M|
|total supply eoy|   1100M|   1188M|   1259M|   1309M|   1362M|   1416M|

Table: Supply per year

While the part devoted to the team and developement may seem high on issuance, the inflation rate makes it lower than the rest of the circulating supply during the 3rd year.

```{.python .run caption="Supply evolution" label="supply_evolution_fig" hide_code=True}
#import matplotlib
#matplotlib.use('AGG')

#import matplotlib.pyplot as plt
import numpy as np
import seaborn

#plt.figure()

#plt.style.use('seaborn-paper')


fig, ax1 = plt.subplots()

year_percents = [10, 8, 6, 4, 4, 4]
new_tokens = []
supply = []
last_supply = 1000
for perc in year_percents:
    minted = last_supply * (perc/100)
    new_tokens.append(minted)
    last_supply += minted
    supply.append(last_supply)

y = [[1000]+supply[:-1], new_tokens]

y_pos = np.arange(len(year_percents))

pal = seaborn.color_palette("Blues")

ax1.stackplot(y_pos,y, labels=['Supply', 'Newly minted'], colors=pal)
ax2 = plt.twinx()
#fig, ax = plt.subplots()
ax2.plot(y_pos, year_percents, label="Inflation rate", color="G")

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0)


ax1.set_xlabel("Year")
ax1.set_ylabel("Supply (Million tokens)")
ax1.set_ylim(0, 2000)
ax2.set_ylabel("Inflation (%)")
ax2.set_ylim(0, 15)

#ax.set_title("'fivethirtyeight' style sheet")
```






