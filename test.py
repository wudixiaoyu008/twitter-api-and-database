from datetime import datetime, date, timedelta

from datetime import timedelta

import tweepy
from tweepy import OAuthHandler
import json


from lab9_config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Authorization setup to access the Twitter API
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

tweets = api.user_timeline(id = 'umsi')
i = 0
for tweet in tweets:
    print (i, tweet.id)
    i += 1

today = datetime.now()
before = today - timedelta(weeks = 2)
d = date(2016, 9, 1)

t= datetime(2016, 9, 1, 0, 0)
t1 = datetime(2016, 9, 1, 0, 1)

print (type(t.year), type(t.month))
print (today>t)

print (before.day)
print (today>before)

print (t<t1)

# f = open('tweets.json', 'w')
# f.write('\naaaaaa')
