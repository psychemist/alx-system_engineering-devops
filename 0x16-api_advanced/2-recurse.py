#!/usr/bin/python3
"""Module 2-recurse queries the Reddit API and returns a list
containing titles of all hot articles for a given subreddit
"""

import json
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API for hot posts in a subreddit

    Args:
        subreddit (str): name of subreddit
        hot_list (list): list of titles of hot posts

    Returns:
        (list): list of strings (post titles) or None
    """
    # set headers
    headers = requests.utils.default_headers()
    headers.update({"User-Agent": "My Agent"})

    # update url after each page with after param and make request
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after is not None:
        url = url + "?after={}".format(after)
    res = requests.get(url, headers=headers, allow_redirects=False)

    # get posts from response json
    data = res.json().get('data', {})
    posts = data.get('children', [])

    if not posts:
        return None

    # append titles to list
    for post in posts:
        hot_list.append(post.get('data').get('title'))

    # get next page and recurse else return
    # after = data.get('after')
    after = data.get('after')
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
