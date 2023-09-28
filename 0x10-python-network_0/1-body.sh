#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response
VAR=$(curl -si "$1" | grep -c 'HTTP/1.1 200 OK'); if [[ "$VAR" == 1 ]]; then curl -s "$1"; fi
