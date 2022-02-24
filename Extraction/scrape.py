#from xmlrpc.client import _datetime
import snscrape.modules.twitter as twitterScrape
import json
import sys
from datetime import date, datetime
from json import dumps
import csv
nom = sys.argv[1]
#"KMbappe"
scraper = twitterScrape.TwitterUserScraper(nom)
tweets = []

for i,tweet in enumerate(scraper.get_items()):
    if i > 1000:
        break
    tweets.append({"id" : tweet.id, "Content": tweet.content , "Username" : tweet.user.username, "Like":tweet.likeCount,"Retweet" :tweet.retweetCount, "ReplyCount" : tweet.replyCount, "Date":str(tweet.date) })

print(tweets)
f = open("{}.json".format(nom),"w")
j = json.dumps(tweets)
f.write(j)
f.close
