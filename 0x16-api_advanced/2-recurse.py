#!/usr/bin/python3
"""
Module pagination
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """
    A recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    if after is None:
        return hot_list
    if after:
        url = url + "?after=" + after

    try:
        res = requests.get(url, allow_redirects=False,
                           headers={'User-Agent': 'Pagination-Example'})
        res = res.json()
        data = res.get('data').get('children')
        after = res.get('data').get('after')
        for post in data:
            hot_list.append(post.get('data').get('title'))
        return recurse(subreddit, hot_list, after)
    except Exception:
        return None
