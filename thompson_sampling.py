# Thompson Sampling

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

dataset = pd.read_csv('Ads_CTR_Optimisation.csv')

# Implimenting Thompson Sampling
N = 10000

# No. of ads
d = 10

ads_selected = []
num_of_rewards1 = [0] * d 
num_of_rewards0 = [0] * d

total_reward = 0

# calculating the average reward and confindence interval
# of ad i upto round n
# also finding out number of selections of a particular ad and their rewards 
for n in range(0, N):
    ad = 0
    max_random = 0
    for i in range(0, d):
        random_beta = random.betavariate(num_of_rewards1[i]+1, num_of_rewards0[i] + 1)
        if random_beta > max_random:
            max_random = random_beta
            ad = i
    ads_selected.append(ad)
    reward = dataset.values[n, ad]
    if reward == 1:
        num_of_rewards1[ad] += 1
    else:
        num_of_rewards0[ad] += 1
    total_reward += reward
    
# Visualization of results
plt.hist(ads_selected)
plt.title("Histogram of ad selections")
plt.xlabel('Ads')
plt.ylabel('Number of times each ad was selected')
plt.show()






