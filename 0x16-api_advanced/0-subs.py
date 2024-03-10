#!/usr/bin/python3
""""getting number of subs"""
import requests
from sys import argv

def number_of_subscribers(subreddit):
    """returns number of subscribers  for a subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')
    else:
        return 0

if __name__ == "__main__":
    number_of_subscribers(argv[1]) 
