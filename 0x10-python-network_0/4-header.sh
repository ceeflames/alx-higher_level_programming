#!/bin/bash
#Bash script that takes in a URL as an argument, sends GET request to the URL, displays the body of the response
curl -sH "X-School-User_Id: 98" "$1"
