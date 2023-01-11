#!/usr/bin/python3
"""
Module top ten
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        hots = requests.get(url, allow_redirects=False,
                            headers={'User-Agent': 'MyChromeBook'})
        posts = hots.json().get('data').get('children')
        for idx, children in enumerate(posts):
            if idx == 10:
                break
            print(children.get('data').get('title'))

    except Exception:
        print(None)
