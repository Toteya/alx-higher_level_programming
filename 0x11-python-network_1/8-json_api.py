#!/usr/bin/python3
"""
module 8-json_api
Sends a POST request to http://0.0.0.0:5000/search_user displays the id and
name if the respose body is properly JSON formatted
"""
import requests
import sys

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    try:
        payload = {'q': sys.argv[1]}
    except IndexError:
        payload = None

    response = requests.post(url, data=payload)
    try:
        body_json = response.json()
        if not body_json:
            print("No result")
        else:
            print("[{}] {}".format(body_json.get('id'), body_json.get('name')))
    except Exception:
        print("Not a valid JSON")
