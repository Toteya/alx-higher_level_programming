#!/usr/bin/python3
"""
module 5-hbtn_header
Sends a request the passed URL and displays the value of the variable
X-Request-Id from the response header
"""
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
