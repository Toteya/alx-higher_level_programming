#!/bin/bash
# This script sends a request to a URL and displays the size of the body of the http response
curl -sI "$1" | grep 'Content-Length' | cut -d ' ' -f 2
