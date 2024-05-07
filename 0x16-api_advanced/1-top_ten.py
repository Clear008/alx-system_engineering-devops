#!/usr/bin/python3
"""Contains the function top_ten"""

import requests

def top_ten(subreddit):
    """Returns the top ten posts for a given subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'CustomBot/1.0'}
    rsp = requests.get(url, headers=headers, allow_redirects=False)

    if rsp.status_code == 200:
        data = rsp.json().get("data", {}).get("children", [])
        top10_posts = "\n".join(post["data"]["title"] for post in data)
        print(top10_posts)
    else:
        print(None)
