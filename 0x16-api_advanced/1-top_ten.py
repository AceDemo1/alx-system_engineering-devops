#!/usr/bin/python3
"""This module defines the list of all subscribers on reddit"""
import requests


def top_ten(subreddit):
    """This method requests the api reddit to return the top ten
    hot post for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'elodieriou3685'}
    params = {'limit': 10}

    req_reddit = requests.get(url,
                              headers=headers,
                              params=params,
                              allow_redirects=False)
    if req_reddit.status_code > 300:
        print("None")
        return

    hot = req_reddit.json().get('data').get('children')
    for top in hot:
        print(top.get('data').get('title'))
