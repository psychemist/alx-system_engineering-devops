"""Queries redit api and returns blanc sjdkvbd jk
"""
import requests

def number_of_subscribers(subreddit):
    """Queries API and returns number of subscribers
    Args:
        subreddit (str): subreddit to be queried

    Returns:
        int: number of subs
        """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-agent': 'Mozilla/5.0'}  # Add a user-agent header to prevent 429 error

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except (requests.RequestException, KeyError):
        return 0
