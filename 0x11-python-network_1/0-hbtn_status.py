#!/usr/bin/python3
"""
Module: 0-hbtn_status
Fetches http://alx-intranet.hbtn.io/status
"""
import urllib.request


def main():
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        page = response.read()
        content = page.decode("utf-8")
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(content))


if __name__ == '__main__':
    main()
