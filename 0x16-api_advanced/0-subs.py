#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent', 'Customer User Agent'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if reponse.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else
        return 0
