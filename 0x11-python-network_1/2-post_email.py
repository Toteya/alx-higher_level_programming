#!/usr/bin/python3
"""
module 2-post_email
Sends a POST request to the passed URL with the email as parameter
"""

import sys
import urllib.request
import urllib.parse

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page)
