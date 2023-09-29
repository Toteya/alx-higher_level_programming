#!/usr/bin/python3
"""
Module 1-hbtn_header
Sends a request to a URL and displays the value of the X-Request-Id
"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.getheader('X-Request-Id'))
