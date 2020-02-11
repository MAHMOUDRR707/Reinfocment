#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#data processing
data =pd.read_csv('Ads_CTR_Optimisation.csv')


import  random  as ra
d=10
N=10000
number_of_1=[0]*d
number_of_0=[0]*d
ads_selected=[]
total_rewards=0
for n in range(N):
    ad=0
    max_random=0
    for i in range(d):
           random_bound= ra.betavariate(number_of_1[i]+1,number_of_0[i]+1)
           if random_bound>max_random :
               max_random=random_bound
               ad=i
    ads_selected.append(ad) 
    rewards=data.values[n,ad]
    if rewards==1:
      number_of_1[ad]+=1
    elif rewards==0:
         number_of_0[ad]+=1
    total_rewards+=rewards
plt.hist(ads_selected)
plt.tittle('ads')
plt.xlabel('number of ads')
plt.yalbel('number of selection')
plt.show()
               
               


