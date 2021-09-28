#!/usr/bin/python3
""" script that verify in the api number of subscriptors of reddit """
import requests
from urllib import response


def number_of_subscribers(subreddit):
    all_info_reddit = requests.get(
                                   "https://www.reddit.com/r/{}/about.json"
                                   .format(subreddit),
                                   headers={'User-Agent': 'Ana'},
                                   allow_redirects=False)

    if all_info_reddit.status_code == 200:
        return all_info_reddit.json().get("data").get("subscribers")
    else:
        return 0
