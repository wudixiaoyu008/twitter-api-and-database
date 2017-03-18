import tweepy
from tweepy import OAuthHandler
import json
from datetime import datetime, date, timedelta


from lab9_config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# Authorization setup to access the Twitter API
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# fetch tweets from umsi after 09/01/2016

with open('tweets.json', 'w') as json_file:
    t = datetime(2016, 9, 1, 0, 0)
    post_day = datetime.now()
    page = 1
    while post_day >= t:   #循环时考虑年份和月份，作为判断条件
        tweets = api.user_timeline(id = 'umsi', page = page) #, include_rts = True
        if tweets:
            for tweet in tweets:
                post_day = tweet.created_at    # datetime object

                if post_day >= t:
                    json_tweet = json.dumps(tweet._json)
                    json_file.write(json_tweet)
                    json_file.write('\n')

                if post_day < t:
                    break

        else:
            break
        page += 1

json_file.close()



# fetch the neighors that mentioned by umsi, count the nubmer
neighbors_username = dict()

f = open('tweets.json', 'r')
for line in f:
    line = json.loads(line)
    mentioned_author = line['entities']['user_mentions']
    for item in mentioned_author:
        # if item['id'] != 18033550:
        neighbors_username[item['screen_name']] = neighbors_username.get(item['screen_name'], 0) + 1


######## sort dict based on the value, return a list of tuple, different from the task3a
sorted_neighbors = sorted(neighbors_username.items(), key=lambda x: x[1], reverse = True)

# neighbors list included 'umsi'
list_neighbors = [ neighbor[0] for neighbor in sorted_neighbors]

f.close()

# count the line nubmer in tweet.json file
count_umsi = sum(1 for line in open('tweets.json'))


with open('tweets2.json', 'w') as json2_file:
    t = datetime(2016, 9, 1, 0, 0)
    total = 0
    while total - count_umsi < 0:
        for neighbor in list_neighbors[1:]:
            tweets = api.user_timeline(id = neighbor)
            if tweets:
                for tweet in tweets:
                    post_day = tweet.created_at
                    if post_day >= t:
                        json_tweet = json.dumps(tweet._json)
                        json2_file.write(json_tweet)
                        json2_file.write('\n')
                        total += 1
                        if total - count_umsi >= 0:
                            break
                    else:
                        break

                if total - count_umsi >= 0:
                    break

            else:
                break

json2_file.close()
