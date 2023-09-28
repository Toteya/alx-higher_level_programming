#!/bin/bash
# This script sends an http JSON POST request to a URL
curl -sX POST -d @"$2" -H "Content-Type: application/json" "$1" 
