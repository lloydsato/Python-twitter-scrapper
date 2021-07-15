import tweepy
import pandas as pd

# Enter user credentials to authenticate api
# Create twitter developer account to get access to the below mentioned credentials

key = "Enter your code\n"
secret = "Enter your code\n"
token = "Enter your code\n"
token_secret = "Enter your code\n"

authentication = tweepy.OAuthHandler(key, secret)
authentication.set_access_token(token, token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

# creating a list of tweets
tweets = []

# Enter username to scrap tweets from
uname = input("Enter the username to scarp tweet from\n")

# Total number of tweets you need
tweetno = input("Enter the number of tweets needed\n")


def tweets_to_csv(uname, tweetno):
    for tweet in api.user_timeline(id=uname, count=tweetno):
        tweets.append((tweet.created_at, tweet.id, tweet.txt))

        df = pd.DataFrame(tweets, columns=['date', 'Tweet_ID', 'Message'])
        df.to_csv('scrapped_tweets')


tweets_to_csv(uname, tweetno)
