#!/usr/bin/python3
""""getting number of subs"""
from requests import get
from sys import argv

def number_of_subscribers(subreddit):
    """returns the number of subs"""
    header = {
        "User-Agent": "alx:lin.api.adv:v1.0.0 (by /u/gena)" 
    }
    count = get('https://www.reddit.com/r/{}/about.json'.format(
        subreddit), headers=header).json()
    try:
        return count.get("data").get("subscribers")
    except:
        return 0

if __name__ == "__main__":
    number_of_subscribers(argv[1]) 
