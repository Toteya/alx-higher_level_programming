#!/usr/bin/python3
"""
module 7-error_code
Sends a request to a URL and displays the body of the response or
otherwise, the error status code
"""
import sys
import requests

if __name__ == '__main__':
    url = sys.argv[1]
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
