import tweepy

from koo import koo
from secrets import app_key, app_secret, token_key, token_secret

auth = tweepy.OAuthHandler(app_key, app_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)


def tweet():
    api.update_status(status=koo())


if __name__ == '__main__':
    tweet()
