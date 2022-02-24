
# pour run tu lance le fichier avec le nom du compte twitter en argument il genere un fichier csv 
import snscrape.modules.twitter as sntwitter
import json
import sys
from datetime import date, datetime
from json import dumps
import pandas as pd
import csv

maxTweets = 1000
nom = sys.argv[1]
#"KMbappe"

# Creating list to append tweet data to
tweets_list1 = []

# Using TwitterSearchScraper to scrape data 
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(nom).get_items()):
    #if i>maxTweets:
    #    break
    #tweets_list1.append([tweet.id, tweet.content, tweet.user.username,tweet.likeCount,tweet.retweetCount,tweet.replyCount,tweet.quoteCount,tweet.date,])
    tweets_list1.append([tweet.content])

# Creating a dataframe from the tweets list above
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Text'])

# Display first 5 entries from dataframe
# tweets_df1.head()

# Export dataframe into a CSV
tweets_df1.to_csv('MB7.csv', sep=',', index=False)
'''
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'user-tweets.csv'
jsonFilePath = r'dataMbappe.json'
csv_to_json(csvFilePath, jsonFilePath)


--------------------------------------------
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'user-tweets.csv'
jsonFilePath = r'data.json'
csv_to_json(csvFilePath, jsonFilePath)
--
#print(f"{i} content: {tweet.content}") pour afficher sur la console 
#tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username]) pour afficher  DateTime, tweet id, text, and username from the tweet object.
#ajouter like rettwet comment 
#fonction cal le total et faire la meme chose 3 '''