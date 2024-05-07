#!/usr/bin/python3
"""function that queries the Reddit API and returns a list
containing the titles of all hot articles"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """function that queries the Reddit API and returns a list
containing the titles of all hot articles"""
    
    if after is None:
        return []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    url += f"?limit=100&after={after}"
    headers = {'user-agent': 'request'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return None
    json_re = response.json()
    hot_posts_json = json_re.get("data").get("children")
    for post in hot_posts_json:
        hot_list.append(post.get("data").get("title"))
    return hot_list + recurse(subreddit, [], json_re.get("data").get("after"))
