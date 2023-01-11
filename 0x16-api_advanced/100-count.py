#!/usr/bin/python3
"""
Module pagination
"""
import requests


def count_words(subreddit, word_list, after=None, words={}):
    """
    A recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    try:
        payload = {'after': after}
        res = requests.get(url, allow_redirects=False,
                           params=payload,
                           headers={'User-Agent': 'Pagination-Example'})
        res = res.json()
        posts = res.get('data').get('children')
        after = res.get('data').get('after')
        for post in posts:
            title = post.get('data').get('title')
            for word in word_list:
                try:
                    words[word] += title.lower().split().count(word.lower())
                except KeyError:
                    words[word] = title.lower().split().count(word.lower())
        if after is None:
            lst = sorted(words.items(), key=lambda t: (-a[1], a[0]))
            for key, value in lst:
                if value:
                    print("{:s}: {:s}".format(key, value))
            return
        return count_words(subreddit, word_list, after, words)
    except Exception:
        return None
