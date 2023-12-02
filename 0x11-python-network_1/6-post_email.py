#!/usr/bin/python3
"""
    Python script that takes in a URL
    an email address, sends a POST request to the passed URL
    with the email as a parameter, and
    finally displays the body of the response.
"""

if __name__ == '__main__':
    import requests
    import sys

    email = {'email': sys.argv[2]}
    url = requests.post(sys.argv[1], data=email)
    print(url.text)
