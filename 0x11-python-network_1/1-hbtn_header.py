#!/usr/bin/python3
"""
    Python script that takes in a URL
    sends a request to the URL
    displays the value of the X-Request-Id variable
    found in the leader of the response
"""

if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        x_request_id = response.getheader("X-Request-Id")
        print(x_request_id)
