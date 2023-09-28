#!/bin/bash
# This script prints the HTTP methods that the server will accept
curl -sI "$1" | grep 'Allow' | cut -d ':' -f 2 | sed 's/^\s//'
