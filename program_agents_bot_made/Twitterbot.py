#import the necessary libraries
import tweepy
import time

#enter your Twitter API credentials
consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

#authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#create a list of tweets
tweets = ["This is my first automated tweet!",
          "Check out our new product!",
          "Follow us for more updates!"]

#loop through the list of tweets and post them
for tweet in tweets:
    api.update_status(tweet)
    time.sleep(30) #sleep for 30 seconds before posting the next tweet