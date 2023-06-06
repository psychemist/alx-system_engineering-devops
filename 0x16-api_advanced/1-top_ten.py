#!/usr/bin/python3
"""Module 1-top_ten queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of first ten hot posts

    Args:
        subreddit (str): Reddit subreddit to be queried
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "My Agent"}

    res = requests.get(url, headers=headers).json()
    data = res.get('data', {}).get('children')

    if not data:
        print(None)
    else:
        for post in data[:10]:
            print(post['data']['title'])
