# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 12:21:13 2019

@author: Karan Raj
"""
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import datetime

def tweet_scroller(url):

    browser.get(url)
    
    #define initial page height for 'while' loop
    lastHeight = browser.execute_script("return document.body.scrollHeight")
    
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        #define how many seconds to wait while dynamic page content loads
        time.sleep(8)
        newHeight = browser.execute_script("return document.body.scrollHeight")
        
        if newHeight == lastHeight:
            break
        else:
            lastHeight = newHeight
            
    html = browser.page_source
    browser.close()
    return html
def scrapper(url):
    soup = BeautifulSoup(tweet_scroller(url), "html.parser")
    for i in soup.find_all('li', {"data-item-type":"tweet"}):
        username=i.div.a['href'].lstrip('/')
        tweet_url='https://twitter.com'+i.div['data-permalink-path']
        screen_name=i.div['data-name']
        tweet=i.find('div', {'class': "js-tweet-text-container"})
        text= (tweet.get_text().replace('\n','') if i.find('div', {'class': "js-tweet-text-container"}) is not None else "")
        time=(i.small.a['title'] if i.small is not None else "")
        tag_text = text.replace("#"," #")
        tag_text = tag_text.replace("@"," @")
        hashs = {tex.strip("#") for tex in tag_text.split() if tex.startswith("#")}
        tagged = {tex.strip("@") for tex in tag_text.split() if tex.startswith("@")}
        footer=i.find('div', {'class': "stream-item-footer"}).div        
        replies=footer.span.span['data-tweet-stat-count'] 
        retweets=footer.find('span',{'class':'ProfileTweet-action--retweet u-hiddenVisually'}).span['data-tweet-stat-count']
        likes=footer.find('span',{'class':'ProfileTweet-action--favorite u-hiddenVisually'}).span['data-tweet-stat-count']
        writecsv(tweet_url,username,screen_name,time,hashs,tagged,text,replies,retweets,likes)
    return 0
def writecsv(tweet_url,username,screen_name,time,hashs,tagged,text,replies,retweets,likes):
    with open('D:/PGDBA/IIT/CN/Project/media/indiaeconomy.csv', 'a',encoding='utf-8') as csvFile:
        writer = csv.writer(csvFile, lineterminator='\n', delimiter=',')
        if(str(hashs)=='set()'):
            hashs=0
        if(str(tagged)=='set()'):
            tagged=0
        row=[tweet_url,username,screen_name,time,hashs,tagged,text,replies,retweets,likes]
        writer.writerow(row)
    csvFile.close()
    return 0

date1 = datetime.date(2016, 11, 8)
date2 = datetime.date(2016, 12, 31)
day = datetime.timedelta(days=1)

while date1 <= date2:
    dt_st=str(date1)
    date1 = date1 + day
    dt_end=str(date1)
    browser = webdriver.Chrome(executable_path='D:/Coding/ChromeDriver/chromedriver.exe')
    url = 'https://twitter.com/search?q=economy%20AND%20india%20since%3A' + dt_st + '%20until%3A' + dt_end + '&src=typd'                    
    scrapper(url)
        #copyfile("D:/PGDBA/IIT/CN/Project/twitter_hashtag_twitter.com.csv", "D:/PGDBA/IIT/CN/Project/users/"+dt_st+".csv" )
        #os.remove("D:/PGDBA/IIT/CN/Project/twitter_hashtag_twitter.com.csv")