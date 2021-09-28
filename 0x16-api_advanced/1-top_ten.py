#!/usr/bin/python3
""" script that verify in the api the titles of the first 10
    hot posts listed for a given subreddit."""
import requests
from urllib import response


def top_ten(subreddit):
    all_info_reddit = requests.get(
                                   "https://www.reddit.com/r/{}"
                                   "/hot.json?limit=10"
                                   .format(subreddit),
                                   headers={'User-Agent': 'Ana'},
                                   allow_redirects=False)

    if all_info_reddit.status_code == 200:
        for top in all_info_reddit.json().get("data").get("children"):
            print(top.get("data").get("title"))
    else:
        print(None)
        return 0
