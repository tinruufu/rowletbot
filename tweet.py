from os import unlink, path
import random
import string

from mastodon import Mastodon
import mimetypes
import tweepy

from avatar import make_avatar
from koo import koo
from secrets import app_key, app_secret, token_key, token_secret

HERE = path.dirname(__file__)

auth = tweepy.OAuthHandler(app_key, app_secret)
auth.set_access_token(token_key, token_secret)
api = tweepy.API(auth)


class Borbstadon(Mastodon):
    """
    Mastodon, but with avatar uploading that doesn't use base64.
    """

    def set_avatar(self, media_file, mime_type=None):
        if mime_type is None and path.isfile(media_file):
            mime_type = mimetypes.guess_type(media_file)[0]
            media_file = open(media_file, 'rb')

        if mime_type is None:
            raise RuntimeError('Could not determine mime type')

        random_suffix = ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(10)
        )

        return self._Mastodon__api_request(
            'PATCH', '/api/v1/accounts/update_credentials', files={'avatar': (
                'borb_{}{}'.format(random_suffix,
                                   mimetypes.guess_extension(mime_type)),
                media_file, mime_type,
            )},
        )


mastodon = Borbstadon(
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


def set_avatar():
    av_path = make_avatar()
    try:
        api.update_profile_image(av_path)
        mastodon.set_avatar(av_path)
    finally:
        unlink(av_path)


if __name__ == '__main__':
    set_avatar()
    status = tweet()
    if status is not None:
        toot(status)
