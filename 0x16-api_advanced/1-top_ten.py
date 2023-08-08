#!/usr/bin/python3
"""
Module prints titles of
the first 10 hot posts.
"""
import requests


def top_ten(subreddit):
    """
    Function returns prints titles of the first
    10 hot posts listed for a given subreddit.
    """
    headers = {
        'User-Agent', 'Customer User Agent'
    }
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if reponse.status_code == 200:
        data = response.json()
        posts = data['data']['childrens']
        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)
