from os import unlink, path
from time import sleep

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
    from raw_mastodon_creds import login, password
    from selenium.webdriver import PhantomJS

    try:
        browser = PhantomJS(service_args=['--webdriver-loglevel=DEBUG'])
        browser.set_window_size(1280, 720)
        browser.implicitly_wait(10)
        browser.get(mastodon.api_base_url + '/auth/sign_in')
        browser.find_element_by_id('user_email').send_keys(login)
        browser.find_element_by_id('user_password').send_keys(password)
        browser.find_element_by_css_selector('button[type="submit"]').click()
        sleep(5)
        browser.get(mastodon.api_base_url + '/settings/profile')
        browser.find_element_by_id('account_avatar').send_keys(av_path)
        browser.find_element_by_css_selector('button[type="submit"]').click()
        browser.find_element_by_css_selector('body')
        sleep(2)
    except:
        browser.save_screenshot(path.join(HERE, 'screenshot.png'))
        raise
    finally:
        browser.quit()


def set_avatar():
    av_path = make_avatar()
    try:
        api.update_profile_image(make_avatar())
        set_mastodon_avatar(av_path)
    finally:
        unlink(av_path)


if __name__ == '__main__':
    set_avatar()
    status = tweet()
    if status is not None:
        toot(status)
