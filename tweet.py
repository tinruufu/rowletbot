import tweepy

from koo import koo
from secrets import app_key, app_secret, token_key, token_secret

auth = tweepy.OAuthHandler(app_key, app_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)


def pad(status):
    zwsp = '\u200b'
    return status[0] + zwsp + status[1:]


def tweet():
    status = koo()
    attempts = 0

    while True:
        attempts += 1

        try:
            api.update_status(status=status)
        except tweepy.TweepError as e:
            if e.api_code == 187 and attempts < 10:
                # this is a dupe
                status = pad(status)
            else:
                raise
        else:
            break


if __name__ == '__main__':
    tweet()