import os
import twitter
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

# api.update_status('tweepy!')


def poststatus(s, p):
    print('no')


def poststatus2(picture):
    # res = api.media_upload(filename=picture)
    status = False
    try:
        status = api.update_with_media(filename=picture)
    except tweepy.error.TweepError as e:
        print(f"Error posting tweet. {e}")
        return status
    # media_ids = [res.media_id_string]
    # result = api.update_status(media_ids)
    # print(f"{res}")
    # print(f"{media_ids}")
    # print(f"{result}")
    # print(status.created_at)
    return status

#
#
# using tweepy end

# api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
#                   access_token_key=access_token_key, access_token_secret=access_token_secret)


# print(api.VerifyCredentials())

# # works vv


# def poststatus(msg, picture):
#     api.PostUpdate(status=msg, media=picture)
# # works ^^


# # def poststatus(picture):
# #     print("Received picture")
# #     # print(api.UploadMediaSimple(picture))
# #     api.UploadMediaChunked(media=picture)

# def poststatus2(picture):
#     api.UploadMediaSimple(media=picture)
