import os
import tweepy
from dotenv import load_dotenv, find_dotenv
load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token_key = os.getenv("ACCESS_TOKEN_KEY")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# using tweepy start
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)


def poststatus(picture):
    status = False
    try:
        status = api.update_with_media(filename=picture)
    except tweepy.error.TweepError as e:
        print(f"Error posting tweet: {e}")
        return status
    return status


# ToDo: reformat to OOP: MediaWorker
# Include both Twitter and Instagram
