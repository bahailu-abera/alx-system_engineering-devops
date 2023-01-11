#!/usr/bin/python3
"""
Request the top ten hot posts
"""
import requests


def count_words(subreddit, word_list, after=None, my_dict={}):
    """
    Gets the top ten hot post of a subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    payload = {'after': after}
    response = requests.get(url,
                            allow_redirects=False,
                            params=payload,
                            headers={'User-Agent': 'Pear'})
    if response and response.status_code == 200:
        post_list = response.json().get('data').get('children')
        for children in post_list:
            title1 = children.get('data').get('title')
            for word in word_list:
                try:
                    my_dict[word] += title1.lower().split().count(word.lower())
                except KeyError:
                    my_dict[word] = title1.lower().split().count(word.lower())
        after = response.json().get('data').get('after')
        if (after is None):
            for key, val in sorted(my_dict.items(),
                                   key=lambda x: (-1*x[1], -1*x[0])):
                if (val != 0):
                    print("{}: {}".format(key.lower(), val))
            return
        return count_words(subreddit, word_list, after, my_dict)
    else:
        return
