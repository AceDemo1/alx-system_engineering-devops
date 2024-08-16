#!/usr/bin/python3
"""This module defines the list of all subscribers on reddit"""
import requests


def number_of_subscribers(subreddit):  
    """This method requests the api reddit to return the number
    of all subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'elodieriou3685'}

    req_reddit = requests.get(url, headers=headers, allow_redirects=False)
    if req_reddit.status_code > 300:
        return 0

    subscribers = req_reddit.json().get('data').get('subscribers')
    return subscribers  
