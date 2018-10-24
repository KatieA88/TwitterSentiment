#first import the packages we need
import json
import pandas as pd
import re
import csv
import numpy as np
    

#read the data into an array
tweets_data_path = '/Users/katieadams/TwitterSentiment/twitter_data.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

#structure into dataframe and add text, lanaguage and country columns
tweets = pd.DataFrame()

tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
   
#remove non english tweets
tweets = tweets[tweets.lang == 'en'] 

#create df of Banks
banks = tweets[tweets['text'].str.contains("barclays|hsbc|lloyds|rbs|santander|halifax")]

#create df of Challenger Banks
ch_banks = tweets[tweets['text'].str.contains("monzo|revolute|atom bank|metro bank")]

#save to csv
banks.to_csv('banks.csv', sep = ',', encoding = 'utf-8')
ch_banks.to_csv('ch_bank.csv', sep = ',', encoding = 'utf-8')


   
