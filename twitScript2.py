import os
import time
import requests
from twitter import *
import pprint
import json
# import sys
# import urllib
# import pusher

import mongoengine
import models

# --------- Database Connection ---------
# MongoDB connection to MongoLab's database
mongoengine.connect('mydata', host='mongodb://poetry:everywhere@ds053708.mongolab.com:53708/twitterpoetry')
#app.logger.debug("Connecting to MongoLabs")


oauth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,CONSUMER_KEY, CONSUMER_SECRET)
twitter = Twitter(auth = oauth)

url = 'http://text-processing.com/api/sentiment/'

firstTweets = twitter.statuses.mentions_timeline(count=100, include_retweets=True, exclude_replies=False)
for tweets in firstTweets:
    firstSet = models.Tweets(text=tweets['text'], username=tweets['user']['screen_name'], created=tweets['created_at'])
    firstSet.save()

while True:
    newTweets = twitter.statuses.mentions_timeline(count=100, include_retweets=True, exclude_replies=False)
    for tweets in newTweets:
       #put tweets into the database if they aren't already there
       newTweet, created = models.Tweets.objects.get_or_create(text=tweets['text'], username=tweets['user']['screen_name'], created=tweets['created_at'])
       time.sleep(5) # sleep / pause execution 5 seconds


