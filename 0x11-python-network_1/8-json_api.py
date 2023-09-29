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
    letter = sys.argv[1]
    payload = {'q': letter}

    response = requests.post(url, data=values)
    print(response.json())
