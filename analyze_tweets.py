#analyze_tweets.py

import sqlite3
import nltk
import re

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()


print('***** MOST FREQUENTLY MENTIONED AUTHORS *****')

query = 'SELECT author_id FROM Mentions'
cur.execute(query)

all_mentions = dict()
for row in cur:
    all_mentions[row[0]] = all_mentions.get(row[0], 0) + 1

# list of tuple includes sorted mentions
sorted_mentions = sorted(all_mentions.items(), key=lambda x: x[1], reverse = True)

list_mentions = [ mention[0] for mention in sorted_mentions]

i = 0
for item in sorted_mentions[0:10]:
    query = 'SELECT username FROM Authors WHERE author_id=\'' + str(item[0]) + '\''
    cur.execute(query)
    for row in cur:
        name = row[0]
        print (name, 'is mentioned', sorted_mentions[i][1], 'times')
        i += 1


print('*' * 20, '\n\n') # dividing line for readable output




print('***** TWEETS MENTIONING AADL *****')

query = 'SELECT tweet_text FROM Tweets JOIN Authors JOIN Mentions ON Tweets.tweet_id = Mentions.tweet_id AND Authors.author_id = Mentions.author_id WHERE username = \'aadl\''
cur.execute(query)

for row in cur:
    print (row[0], '\n')

print('*' * 20, '\n\n')



print('***** MOST COMMON VERBS IN UMSI TWEETS *****')

query = 'SELECT tweet_text FROM Tweets WHERE author_id = 18033550'
cur.execute(query)
umsi_tweet = ''
for row in cur:
    each_text = row[0] + ' '
    umsi_tweet += each_text

# replace specific ['@', '-', '_', b'\xe2\x80\xa6'.decode(), 'umsi', 'umsiasb17', 'umich', 'https'] with ''
umsi_tweet = re.sub(r'@|(umsi)', ' ', umsi_tweet)

tokens = nltk.word_tokenize(umsi_tweet)
tagged = nltk.pos_tag(tokens)

vb_umsi = dict()
for item in tagged:
    if item[1] == 'VB':
        vb_umsi[item[0]] = vb_umsi.get(item[0], 0) + 1

sorted_vb_umsi = sorted(vb_umsi.items(), key = lambda x: x[1], reverse = True)

for item in sorted_vb_umsi[:10]:
    print (item[0], '(', item[1], 'times)')



print('*' * 20, '\n\n')



print('***** MOST COMMON VERBS IN UMSI "NEIGHBOR" TWEETS *****')

query = 'SELECT tweet_text FROM Tweets WHERE author_id <> 18033550'
cur.execute(query)
neighbor_tweet = ''
for row in cur:
    each_text = row[0] + ' '
    neighbor_tweet += each_text

neighbor_tweet = re.sub(r'@|(umsi)|(drchuck)', ' ', neighbor_tweet)

tokens = nltk.word_tokenize(neighbor_tweet)
tagged = nltk.pos_tag(tokens)

vb_neighbor = dict()
for item in tagged:
    if item[1] == 'VB':
        vb_neighbor[item[0]] = vb_neighbor.get(item[0], 0) + 1

sorted_vb_neighbor = sorted(vb_neighbor.items(), key = lambda x: x[1], reverse = True)

for item in sorted_vb_neighbor[:10]:
    print (item[0], '(', item[1], 'times)')

print('*' * 20, '\n\n')


conn.close()
