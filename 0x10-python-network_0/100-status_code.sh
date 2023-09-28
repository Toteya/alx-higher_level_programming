#!/bin/bash
# The script send an HTTP request and displays the status code of the HTTP response
curl -s -o /dev/null -w "%{http_code}" "$1"
