#!/usr/bin/python3
""" script that verify in the api  recursive function that queries
    the Reddit API and returns a list
    containing the titles of all hot articlest."""
import requests
from urllib import response


def recurse(subreddit, hot_list=[], count=0, after=None):
    all_info_reddit = requests.get(
                                   "https://www.reddit.com/r/{}"
                                   "/hot.json"
                                   .format(subreddit),
                                   params={"count": count, "after": after},
                                   headers={'User-Agent': 'Ana'},
                                   allow_redirects=False)

    if all_info_reddit.status_code == 200:
        for top in all_info_reddit.json().get("data").get("children"):
            print(top.get("data").get("title"))
    else:
        print(None)
        return 0
