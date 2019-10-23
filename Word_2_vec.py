# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 16:21:38 2019

@author: Amit
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

import numpy as np

import re

import pandas as pd

from sklearn import preprocessing

from gensim.models import Word2Vec
nltk.download('punkt')
nltk.download('stopwords')

data=pd.read_csv("D:/IIT_KGP/Complex Networks/Project/Data/combine.csv")

a=pd.DataFrame(data.values[:,6])
a.isnull().sum()
a.dropna()

comb_tweets=[]
for i in range(len(a)):
    comb_tweets=np.hstack((comb_tweets,a.values[i]))

comb_tweets=np.asmatrix(comb_tweets)

combined=comb_tweets[0,0]

for i in range(1,comb_tweets.shape[1]):
    combined=combined+','+comb_tweets[0,i]

result = re.sub(r"http\S+", " ", combined)
t=re.sub(r"#\S+"," ",result)
b=t.replace("/"," ")
c=re.sub(r"@\S+"," ",b)
e=c.replace("-"," ")
f=e.replace("?"," ")
g=f.replace("."," ")
h=g.replace("!"," ")
i=h.replace(","," ")
j=i.replace("&"," ")
k=j.replace(":"," ")
l=k.replace("``"," ")
m=re.sub(r"\xa0\S+"," ",l)
n=re.sub(r"\d"," ",m)
o=n.replace("₹"," ")
p=o.replace("\xa0"," ")
r=p.replace("\'"," ")
s=r.replace("|"," ")
x=re.sub(r"pictwitter\S+"," ",s) 
y=x.replace("‘"," ")  
z=y.replace("("," ")
z1=z.replace("happenbut","happen but")
z2=z1.replace("votelessWe","voteless We")
z3=z2.replace("''"," ")
z4=z3.replace("’"," ")
z5=z4.replace("Rate\u200b"," ")

Z=word_tokenize(z5)
len(Z)

stop_words=set(stopwords.words('english'))

filtered_words=[]

for w in Z:
    if w not in stop_words:
        filtered_words.append(w)
        
len(filtered_words)

unique=set(filtered_words)
unique_words=(list(unique))
len(unique_words)

#checking the adequacy of dictionary
a=np.zeros(len(unique_words))

for i in range(len(unique_words)):
    a[i]=unique_words.count(unique_words[i])

b=0
for i in range(len(unique_words)):
    if (a[i]!=1):
        b=b+1
        

#Dictionary of words in the tweets

dictionary=list(dict.fromkeys(filtered_words))
print(dictionary)
len(dictionary)
dictionary_df = pd.DataFrame(dictionary)
dictionary_df.to_csv("dict.csv")
#Word tokenisation of individual tweets

data.values[:,3]

user=set(data.values[:,3])
username=(list(user))

username[2]
tweet_matrix=np.empty((len(username),2),dtype='>U1028')


for i in range(1,len(username)):
    blank=[]
    blank=data[data.values[:,3]==username[i]]
    comb=blank.values[0,6]
    for j in range(1,blank.shape[0]):
        comb=comb+','+blank.values[j,6]
    tweet_matrix[i,0]=username[i]
    tweet_matrix[i,1]=comb
    
    
tweet_matrix.shape     

tweet_matrix1=tweet_matrix[1:tweet_matrix.shape[0],:]

vector=np.zeros((tweet_matrix1.shape[0],len(unique_words)))

for i in range(tweet_matrix1.shape[0]):
    for j in range(len(unique_words)):
        if ((' '+unique_words[j]+' ') in (' '+tweet_matrix1[i,1]+' ')):
            vector[i,j]=1
        else:
            vector[i,j]=0
vector.sum()        
vector.shape

vec_df = pd.DataFrame(vector)
vec_df.to_csv("users_matrix.csv")

