#!/bin/bash
# Bash script that sends a JSON POST request to a URL first argument, displays the body of response
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
