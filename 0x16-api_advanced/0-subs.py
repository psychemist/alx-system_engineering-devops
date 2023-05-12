#!/usr/bin/python3
"""Module 0-subs queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) of a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """Queries the Reddit API by subreddit

    Args:
        subreddit (str): Reddit subreddit to be queried

    Returns:
        int: number of subscribers (SUCCESS) or 0 (FAIL)
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers)
    data = res.json()
    count = data.get('data').get('subscribers')

    if count is None:
        return 0
    return count
