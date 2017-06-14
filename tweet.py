from base64 import b64encode
from os import unlink, path

from mastodon import Mastodon
import tweepy

from avatar import make_avatar
from koo import koo
from secrets import app_key, app_secret, token_key, token_secret

HERE = path.dirname(__file__)

auth = tweepy.OAuthHandler(app_key, app_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)

mastodon = Mastodon(
    client_id=path.join(HERE, 'mastodon_app_creds.txt'),
    access_token=path.join(HERE, 'mastodon_creds.txt'),
)


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
                status = koo()
            else:
                raise
        else:
            return status


def toot(status):
    mastodon.toot(status)


def set_mastodon_avatar(av_path):
    with open(av_path, 'rb') as av:
        mastodon.account_update_credentials(
            avatar='data:image/png;base64,{}'.format(
                b64encode(av.read()).decode('utf-8')
            )
        )


def set_avatar():
    av_path = make_avatar()
    try:
        api.update_profile_image(av_path)
        set_mastodon_avatar(av_path)
    finally:
        unlink(av_path)


if __name__ == '__main__':
    set_avatar()
    status = tweet()
    if status is not None:
        toot(status)
