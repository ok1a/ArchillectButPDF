import twitter
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv()

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token_key = os.getenv("ACCESS_TOKEN_KEY")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")


api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                  access_token_key=access_token_key, access_token_secret=access_token_secret)


# print(api.VerifyCredentials())


# def poststatus(msg, picture):
#     api.PostUpdate(status=msg, media=picture)
def poststatus(msg, picture):
    api.UploadMediaSimple(media=picture)
