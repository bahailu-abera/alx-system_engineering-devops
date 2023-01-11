#!/usr/bin/python3
"""
Module subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers (not active users, total subscribers)
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    try:
        res = requests.get(url, allow_redirects=False,
                           headers={'User-Agent': 'MyChromeBook'})
        return res.json().get('data').get('subscribers')
    except Exception:
        return 0
