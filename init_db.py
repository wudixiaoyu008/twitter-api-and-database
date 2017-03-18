#init_db.py

import sqlite3

reset = True

conn = sqlite3.connect('tweets.db')
cur = conn.cursor()
# Put code here to create the database and tables
if reset:
	cur.execute("DROP TABLE IF EXISTS Tweets")
	cur.execute("DROP TABLE IF EXISTS Authors")
	cur.execute("DROP TABLE IF EXISTS Mentions")


# Create a table to store Tweets
table_spec = 'CREATE TABLE IF NOT EXISTS '
table_spec += 'Tweets (id INTEGER PRIMARY KEY AUTOINCREMENT, '
table_spec += 'tweet_id INTEGER, author_id INTEGER, tweet_text TEXT, time_stamp TIMESTAMP)'
cur.execute(table_spec)

table_spec = 'CREATE TABLE IF NOT EXISTS '
table_spec += 'Authors (author_id INTEGER, '
table_spec += 'username TEXT)'
cur.execute(table_spec)


table_spec = 'CREATE TABLE IF NOT EXISTS '
table_spec += 'Mentions ('
table_spec += 'tweet_id INTEGER, author_id INTEGER)'
cur.execute(table_spec)
#
# You may want to set this up so that you can also DROP or TRUNCATE tables
# as you are developing so that you can start from scratch when you need to

conn.close()
