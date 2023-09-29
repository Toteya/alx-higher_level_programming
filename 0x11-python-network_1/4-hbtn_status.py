#!/usr/bin/python3
"""
module 4-hbtn_status
Fetches the URL https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == '__main__':
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t - type: {}".format(type(response.text)))
    print("\t - content: {}".format(response.text))
    # print(type(response.read()))
    # print(response.__dict__)
