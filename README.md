# Twitter api and interact with database

### 1. Fetch all UMSI tweets since Sept. 1, 2016 and load into a database

   Using the Twitter REST API, fetch all tweets that have been published by the School of Information twitter account (which publishes under the twitter handle ‘umsi)’ since the start of the 2016-2017 school year. Load all of the tweets into a database table Tweets, storing at least the tweet ID, author, timestamp, and text.
   
### 2. Fetch tweets from UMSI’s most-mentioned accounts and load them into the database, too.

   In Twitter, a tweet can “mention” another account using the syntax @user. Create a database structure that will capture the many-to-many relationship between tweets and mentioned authors. Then, add a bunch of tweets to the database that were published by UMSI’s mentioned authors

### 3. Analyze the tweets
   
   * Print the 10 most frequently mentioned authors in the overall corpus (including both umsi and umsi-mentioned author tweets), and the number of mentions they received.
   * Print all tweets that mention the AADL twitter account (username = ‘aadl’). Tweets by both umsi and the mentioned authors should be included. No tweet should appear more than once.
   * Print the 10 most commonly occurring “Basic Verbs” in the umsi tweets as well as from the “mentioned author” tweets. For these analysis you will use NLTK, and you will want to focus on the ‘VB’ part of speech tag that is part of the default POS Tagger in NLTK.
