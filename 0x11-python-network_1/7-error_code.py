#!/usr/bin/python3
"""
    Python script that takes in a URL
    sends a request to the URL and
    displays the body of the response
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]

    request = requests.get(url)
    status = request.status_code

    if status < 400:
        print(request.text)
    else:
        print("Error code: {}".format(request.status_code))
