from time import sleep
from random import random


def tweet_soon():
    sleep(60 * 60 * random() * 6)
    import tweet
    tweet.set_avatar()
    tweet.tweet()


if __name__ == '__main__':
    tweet_soon()
