#!/usr/bin/python3
"""
Module pagination
"""
import requests


def count_words(subreddit, word_list, after='', words={}):
    """
    A recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    if after is None:
        print("finished")
        print(words)
        lst = sorted([(v, k) for k, v in words.items()], reverese=True)
        for value, key in lst:
            print("{}: {}".format(key, value))
    if after:
        url = url + "?after=" + after

    try:
        res = requests.get(url, allow_redirects=False,
                           headers={'User-Agent': 'Pagination-Example'})
        res = res.json()
        data = res.get('data').get('children')
        after = res.get('data').get('after')
        for post in data:
            title = post.get('data').get('title')
            for word in word_list:
                word = word.lower()
                if word in title.lower():
                    words[word] = words.get(word, 0) + 1
        return count_words(subreddit, word_list, after, words)
    except Exception:
        return None
