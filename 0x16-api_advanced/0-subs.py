"""Queries the Reddit API and returns the number of subscribers"""

import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    
    url = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit))
    headers = {'user-agent': 'request'}
    rsp = requests.get(url, headers=headers, allow_redirects=False)
    if rsp.status_code != 200:
        return 0
    data = rsp.json().get("data")
    return data.get("subscribers")
