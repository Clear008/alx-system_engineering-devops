#!/usr/bin/python3
"""function that queries the Reddit API, parses the title of
all hot articles, and prints a sorted count of given keywords"""
import requests


def count_words(subreddit, word_list, after='', word_dict={}):
    """function that queries the Reddit API, parses the title of
    all hot articles, and prints a sorted count of given keywords"""

    if not word_dict:
        for w in word_list:
            if w.lower() not in word_dict:
                word_dict[w.lower()] = 0
    if after is None:
        w_dict = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for w in w_dict:
            if w[1]:
                print('{}: {}'.format(w[0], w[1]))
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'user-agent': 'redquery'}
    params = {'limit': 100, 'after': after}
    rsp = requests.get(url, headers=header, params=params,
                       allow_redirects=False)

    if rsp.status_code != 200:
        return None
    try:
        h_posts = rsp.json()['data']['children']
        aft = rsp.json()['data']['after']
        for post in h_posts:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]
            for w in word_dict.keys():
                word_dict[w] += lower.count(w)

    except Exception:
        return None
    count_words(subreddit, word_list, aft, word_dict)
