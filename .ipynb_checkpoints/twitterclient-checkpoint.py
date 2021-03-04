'''
Author: Paul Owe
Description: This is a twitter client that handles authentication to twitter via tweepy API.
For authentication you will need API keys from twitter. You can apply here https://developer.twitter.com/en

Note: Keep these keys private.

Last updated: Mar 4, 2021
'''
import os
import sys
from tweepy import API
from tweepy import OAuthHandler
from dotenv import load_dotenv

def get_twitter_auth():
    #set up twitter authentication

    # Return: tweepy.OAuthHandler object

    try:
        load_dotenv()
        consumer_key = os.environ['TWITTER_CONSUMER_KEY']
        consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
        access_token = os.environ['TWITTER_ACCESS_TOKEN']
        access_secret= os.environ['TWITTER_ACCESS_SECRET']
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    return auth


def get_twitter_client():
    #Setu twitter API client.

    # Return tweepy.API object

    auth = get_twitter_auth()
    client = API(auth)
    return client
