# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 02:49:12 2019

@author: chaitanya
"""

import numpy as np
import pandas as pd
from pandas import Series,DataFrame
from textblob import TextBlob
import matplotlib.pyplot as plt
import re

class TweetAnalyzer():
    """
    Functionality for analyzing and categorizing content from tweets.
    """

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def analyze_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1

    

tweet_analyzer = TweetAnalyzer()

df = pd.read_csv('C:\\Users\\chaitanya\\Desktop\\projects\\twitter project\\combine.csv',encoding = "ISO-8859-1")


df['sentiment'] = np.array([tweet_analyzer.analyze_sentiment(tweet) for tweet in df['tweets']])
#print(df.tail(1400))
df