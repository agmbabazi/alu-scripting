#!/usr/bin/python3
"""Print top 10 hot post titles for a subreddit"""
import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'ALU-Reddit-API-Project'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            for post in posts:
                print(post['data'].get('title'))
            return
    except Exception:
        pass
    print(None)
