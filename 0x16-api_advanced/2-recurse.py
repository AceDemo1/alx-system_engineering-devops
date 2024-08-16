#!/usr/bin/python3
"""This module defines the list of all subscribers on reddit"""
import requests


def recurse(subreddit, hot_list=[], after=""):  
    """This method requests the api reddit to return a list containing
    the title of all article for a given subreddit"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'elodieriou3685'}
    params = {'after': after,
              'limit': 100}

    req_reddit = requests.get(url,
                              headers=headers,
                              params=params,
                              allow_redirects=False)
    if req_reddit.status_code > 300:
        return None

    hot = req_reddit.json().get('data')
    after = hot.get('after')
    for result in hot.get('children'):
        hot_list.append(result.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list  
