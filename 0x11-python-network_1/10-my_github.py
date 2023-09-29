#!/usr/bin/python3
"""
module 10-my_github
Takes GitHub credentials and displays user id
"""
import requests
import sys

if __name__ == '__main__':
    url = "https://api.github.com/user"
    user = sys.argv[1]
    token = sys.argv[2]
    headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer {}".format(token),
            "X-GitHub-Api-Version": "2022-11-28"
        }
    response = requests.get(url, headers=headers)
    body = response.json()
    print(body.get('id'))
