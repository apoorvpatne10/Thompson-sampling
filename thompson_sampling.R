# Thompson Sampling

# Importing the dataset
dataset = read.csv('Ads_CTR_Optimisation.csv')

# Implementing Thompson Sampling
N = 10000
d = 10
ads_selected = integer()
num_of_rewards1 = integer(d)
num_of_rewards0 = integer(d)
total_reward = 0

for (n in 1:N){
    
    ad = 0
    max_random = 0
    for(i in 1:d){
        random_beta = rbeta(n = 1,
                            shape1 = num_of_rewards1[i]+1,
                            shape2 = num_of_rewards0[i]+1)
        
        if(random_beta > max_random){
            max_random = random_beta
            ad = i
        }
    }
    
    ads_selected = append(ads_selected, ad)
    reward = dataset[n, ad]
    
    if(reward == 1){
        num_of_rewards1[ad] = num_of_rewards1[ad] + 1
    }
    else{
        num_of_rewards0[ad] = num_of_rewards0[ad] + 1
    }
    
    total_reward = total_reward + reward
}

# Visualizing the results - Histogram
hist(ads_selected, col = 'blue',
     main = 'Histogram of ads selections',
     xlab = 'Ads',
     ylab = 'Number of times each ad was selected')


