#!/usr/bin/python3
from urllib import response
import requests


def number_of_subscribers(subreddit):
    all_info_reddit = requests.get(
                                   "https://www.reddit.com/r/{}/about.json"
                                   .format(subreddit),
                                   headers={'User-Agent': 'Ana'},
                                   allow_redirects=False)

    if all_info_reddit == 200:
        return response.json().get("data").get("subscribers")
    else:
        return (0)
