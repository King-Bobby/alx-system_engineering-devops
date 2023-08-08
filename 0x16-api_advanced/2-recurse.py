#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after="tmp"):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after != "tmp":
        url += "?after={}".format(after)
    headers = {'User-Agent': 'CustomUserAgent'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)

        after = data['data']['after']
        if not after:
            return (hot_list)
    else:
        return (None)
    return recurse(subreddit, hot_list, after)
