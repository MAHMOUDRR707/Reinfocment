#Reinfocment
#USB
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#daat processing
data =  pd.read_csv('Ads_CTR_Optimisation.csv')


#Upper Confidence Bound
import math as mt 
N=10000
d=10
ads_selected = []
numbers_of_selections = [0] * d
sums_of_rewards = [0] * d
total_reward = 0
for n in range (0,N):
    ad = 0
    max_upper_bound = 0
    for i in range(0,d):
         if (numbers_of_selections[i]>0):
             average_wards=sums_of_rewards[i] /numbers_of_selections[i]
             delta_i=mt.sqrt((1.5*mt.log(n+1))/(numbers_of_selections[i]))
             upper_bound=average_wards+delta_i
         else :
             upper_bound= 1e400
         if (upper_bound>max_upper_bound):
            max_upper_bound=upper_bound
            ad=i 
    ads_selected.append(ad)
    numbers_of_selections[ad] = numbers_of_selections[ad] + 1
    rewards=data.values[n,ad]
    sums_of_rewards[ad] = sums_of_rewards[ad] + rewards
    total_reward+=rewards
plt.hist(ads_selected )
plt.tittle('the hight add was selected')
plt.xlabel('n of the ads')
plt.ylabel('n of viewers')
plt.show()
             