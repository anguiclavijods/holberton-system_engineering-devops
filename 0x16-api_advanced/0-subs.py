#!/usr/bin/python3
""" script that verify in the api number of subscriptors of reddit"""
import requests
from urllib import response


def number_of_subscribers(subreddit):
    """ function number of subscribers for verify url and data of users"""
    all_info_reddit = requests.get(
                                   "https://www.reddit.com/r/{}/about.json"
                                   .format(subreddit),
                                   headers={'User-Agent': 'Ana'},
                                   allow_redirects=False)

    if all_info_reddit == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
