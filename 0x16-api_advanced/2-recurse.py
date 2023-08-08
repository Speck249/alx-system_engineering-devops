#!/usr/bin/python3
"""
Module returns top
article titles.
"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Function returns a list containing titles of
    all hot articles for a given subreddit.
    """
    headers = {
        'User-Agent', 'Customer User Agent'
    }
    url = 'https://www.reddit.com/r/{}/' \
          'hot.json?limit=100'.format(subreddit)

    if after:
        url += f'&after={after}'

    response = requests.get(url, headers=headers,
                            allow_redirects=False)

    if reponse.status_code == 200:
        data = response.json()
        posts = data['data']['childrens']

        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']

        if after:
            return recurse(subreddit, hot_list, after=after)
        else:
            return hot_list
    else:
        print(None)
