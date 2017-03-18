import sqlite3
import json

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()

# add database the umsi tweet and author

raw_umsi = dict()
f = open('tweets.json')
for line in f:
    line = json.loads(line)
    none = None
    tweet_id = line['id']
    author_id = line['user']['id']
    tweet_text = line['text']
    time_stamp = line['created_at']
    argument = (none, tweet_id, author_id, tweet_text, time_stamp)
    # tweets_item.append(argument)
    statement = 'INSERT INTO Tweets VALUES (?, ?, ?, ?, ?)'
    cur.execute(statement, argument)
    conn.commit()

    author_mention = line['entities']['user_mentions']
    if author_mention:
        for item in author_mention:
            author_id1 = item['id']
            author_name = item['screen_name']
            raw_umsi[author_id1] = author_name

f.close()

# for k,v in raw_umsi.items():
#     argument = (k, v)
#     statement = 'INSERT INTO Authors VALUES (?, ?)'
#     cur.execute(statement, argument)
#     conn.commit()


# add to databse the tweets of neighbors of umsi

# raw_neighbors = dict()
f = open('tweets2.json')
for line in f:
    line = json.loads(line)
    none = None
    tweet_id = line['id']
    author_id = line['user']['id']
    tweet_text = line['text']
    time_stamp = line['created_at']
    argument = (none, tweet_id, author_id, tweet_text, time_stamp)
    # tweets_item.append(argument)
    statement = 'INSERT INTO Tweets VALUES (?, ?, ?, ?, ?)'
    cur.execute(statement, argument)
    conn.commit()

    author_mention = line['entities']['user_mentions']
    if author_mention:
        for item in author_mention:
            author_id1 = item['id']
            author_name = item['screen_name']
            raw_umsi[author_id1] = author_name
f.close()

for k,v in raw_umsi.items():
    argument = (k, v)
    statement = 'INSERT INTO Authors VALUES (?, ?)'
    cur.execute(statement, argument)
    conn.commit()


# add to Mentions of tweets by 'umsi'
f = open('tweets.json')
for line in f:
    line = json.loads(line)
    tweet_id = line['id']
    mention_neighbor = line['entities']['user_mentions']
    if mention_neighbor:
        for item in mention_neighbor:
            argument = (tweet_id, item['id'])
            statement = 'INSERT INTO Mentions VALUES (?, ?)'
            cur.execute(statement, argument)
            conn.commit()
f.close()

# add to Mentions of tweets by umsi's neighbors
f = open('tweets2.json')
for line in f:
    line = json.loads(line)
    tweet_id = line['id']
    mention_neighbor = line['entities']['user_mentions']
    if mention_neighbor:
        for item in mention_neighbor:
            argument = (tweet_id, item['id'])
            statement = 'INSERT INTO Mentions VALUES (?, ?)'
            cur.execute(statement, argument)
            conn.commit()
f.close()

# SELECT username FROM Authors JOIN Tweets ON Tweets.author_id=Authors.author_id WHERE tweet_id=827203934905364480

#   SELECT COUNT(*) FROM Authors JOIN Mentions ON Authors.author_id = Mentions.author_id JOIN Tweets ON Mentions.tweet_id = Tweets.tweet_id WHERE Tweets.tweet_id = 805816623810703360
