#!/usr/bin/python3
"""
module 3-error_code
Sends a request to passed URL and displays the body of the response or the
error code
"""
import sys
import urllib.request
import urllib.error

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            page = response.read()
            body = page.decode("utf8")
            print(body)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
