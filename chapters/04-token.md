# Aleph Token

## Rewards

Three main sources of reward and token creation are:

- Reward each signed message written to the underlying blockchain
- Reward storage of application data (pin items) and availability of API, both are mandatory for nodes
- POCM NULS token locking in NULS underlying chain (see token distribution section)

Of those rewards, a part will come from monetary creation, and a part from dApp owner incentive to prioritize their apps and their user fees.

If a dApp owner wants to get the benefit of the network without having to rely on third parties only, he can run a node of the network where he prioritizes his dApp data (but he can't completely ignore others, having a backup for his users on other nodes, while he gives the same allowance to other dApps).

## Token use

Most node owners will accept free storage of dApp data, especially at start of the network. Once the data grows bigger, and it begins to become impratical for hosts to have all the data, dApp owners can pay for storage and writes to the blockchain of his dApp data.

Alternatively, application users can pay themselves for the storage of their data (example, big data volume like picture storage applications).

## Token details

Initially, the first issuance of the Aleph utility token will be made as an NRC-20 token. This will be able to be swapped for the native asset at a later date.

If technically possible (part under research):

- the switch between NRC-20 and native Aleph token will be available in both directions.
- the token will also be made available as an ERC-20 token

## Initial token distribution

The exact details of the initial token distribution plan will be announced at a later date. Below is what is currently planned for the token distribution (can be subject to changes).

To reward the NULS community and ecosystem, a large percentage of the supply will be distributed to NULS token holders through the POCM system.

1,000,000,000 (1 billion) tokens will be issued initially.

Of those :

  - 150M will be devoted to airdrop, marketing and bounties (details of airdrop part will be announced through official channels)
  - 150M will be reserved for the NULS community/foundation (100M locked for the POCM mining program and 50M for other incentives)
  - 350M for private / institutionnal investors / OTC sales
  - 350M to the Aleph team (who will use this for bootstrap period rewards, might be able to sell some for development funding, allocate a part for a community or foundation fund or any other use it might deem necessary)

```{.python .run caption="Token Distribution" label="allocation_fig" hide_code=True}
import matplotlib
# import seaborn as sns
from matplotlib import pyplot as plt

matplotlib.use('PDF')
plt.figure()
#plt.use('PDF')

#plt.style.use('seaborn-paper')

# create data
names=('Airdrop, Marketing\n& Bounties\n150M', 'NULS (POCM&Others)\n150M', 'Contributors\n350M', 'Reserved\n350M',)
size=[150,150,350,350]

# Create a circle for the center of the plot
my_circle=plt.Circle( (0,0), 0.7, color='white')
plt.pie(size, labels=names, wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' })
p=plt.gcf()
p.gca().add_artist(my_circle)
```

### NULS staking program (POCM)

In addition to a regular airdrop, NULS holders can lock a part of their NULS tokens to get Aleph tokens.

While their tokens are locked, they will receive Aleph tokens based on the NULS amount they have "staked"/"locked".
The reward will be higher at the start of the POCM period (approximately 10 years) and lower at the end.

Those tokens will come from an initial pool of 200M tokens, locked for that specific purpose. Once that pool dries up at the end of the period, the reward will be lowered and the tokens minted using this program will be taken from the Supply Evolution.

## Supply evolution

Once the full network is ready (see roadmap chapter) and through the described rewards, the token supply will grow by approximately 10% the first year. Then the inflation rate will decrease by 1% each year until it reaches 1% per year and stay at that value.

|                  | 1st year | 2nd year | 3rd year | 4th year | 5th year | 6th year |
|------------------|----------|----------|----------|----------|----------|----------|
| inflation        | 4%       | 3%       | 2%       | 1%       | 1%       | 1%       |
| tokens minted    | 40M      | 31.2M    | 21.42M   | 10.92M   | 11.03M   | 11.14M   |
| total supply eoy | 1040M    | 1071M    | 1092M    | 1103M    | 1114M    | 1125M    |

Table: Supply per year

```{.python .run caption="Supply evolution" label="supply_evolution_fig" hide_code=True }
#import matplotlib
#matplotlib.use('AGG')

#import matplotlib.pyplot as plt
import numpy as np
import seaborn

#plt.figure()

#plt.style.use('seaborn-paper')


fig, ax1 = plt.subplots()

year_percents = [4, 3, 2, 1, 1, 1]
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
