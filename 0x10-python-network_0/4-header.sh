#!/bin/bash
# This script sends a GET request to a URL with a header variable X-School-User-Id=98
curl -sX "GET" -H "X-School-User-Id: 98" "$1"
