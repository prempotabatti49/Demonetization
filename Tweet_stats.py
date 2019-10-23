# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 01:14:51 2019

@author: Amit
"""

import numpy as np

import pandas as pd

from sklearn.preprocessing import LabelEncoder

import matplotlib.pyplot as plt

import collections

data=pd.read_csv("D:/IIT_KGP/Complex Networks/Project/Data/combine.csv")

#Encoding usernames with integers
le=LabelEncoder()

a=le.fit_transform(data.values[:,3].astype(str))

#Calculating tweet counts for each user
users=np.arange(a.min(),a.max()+1) 

tweet_counts=np.zeros(len(users))


for i in range(len(users)):
    for j in range(len(a)):
        if (a[j]==users[i]):
            tweet_counts[i]=tweet_counts[i]+1
            
unique_users=len(tweet_counts)

max_tweets=tweet_counts.max()

min_tweets=tweet_counts.min()

#Plotting the histogram of number of tweets
plt.hist(tweet_counts,bins=np.arange(1,tweet_counts.max()+1))

#Finding number of users for certain number of tweets
count=np.arange(1,tweet_counts.max()+1)

tweets=np.zeros(67)

for i in range(len(tweets)):
    for j in range(len(tweet_counts)):
        if(tweet_counts[j]==count[i]):
            tweets[i]=tweets[i]+1

tweets_final=pd.DataFrame(tweets)
tweets_final.to_csv("tweet_stats.csv")
