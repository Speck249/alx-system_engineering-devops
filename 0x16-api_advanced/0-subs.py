#!/usr/bin/python3
"""
Module retrieves numbers
of reddit subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function returns number of total subscribers
    for a given subreddit.
    """
    headers = {'User-Agent', 'Customer User Agent'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if reponse.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
