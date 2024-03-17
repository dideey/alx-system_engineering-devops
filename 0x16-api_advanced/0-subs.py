#!/usr/bin/python3
""""getting number of subs"""
import requests


def number_of_subscribers(subreddit):
    """returns number of subscribers  for a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0