#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
    else:
        for i in range(10):
            print(response.json().get('data').get('children')[i].get
                  ('data').get('title'))
