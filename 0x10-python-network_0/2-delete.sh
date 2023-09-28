#!/bin/bash
# This script sends a DELETE requst to a URL and displays the body of the http response
curl -sX "DELETE" "$1"
