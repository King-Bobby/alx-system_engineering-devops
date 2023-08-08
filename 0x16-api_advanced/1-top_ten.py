#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'CustomUserAgent'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for i, posts in enumerate(posts[:10]):
            title = posts['data']['title']
            print("{}".format(title))
    else:
        print(None)
