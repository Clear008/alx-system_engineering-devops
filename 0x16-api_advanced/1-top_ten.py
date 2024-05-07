#!/usr/bin/python3
"""contains the function top_ten"""

import requests


def top_ten(subreddit):
    """returns the top ten posts for a given subreddit"""
    
    url = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit))
    headers = {'user-agent': 'request'}
    rsp = requests.get(url, headers=headers, allow_redirects=False)
    if rsp.status_code != 200:
        print(None)
        return
    data = rsp.json().get("data").get("children")
    top10_posts = "\n".join(post.get("data").get("title") for post in data)
    print(top10_posts)
