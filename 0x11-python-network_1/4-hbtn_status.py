#!/usr/bin/python3
"""
    Python script that fetches
    https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import requests

    url = requests.get('https://alx-intranet.hbtn.io/status')
    data = url.text
    print("Body response:")
    print(f'\t- type: {type(data)}')
    print(f'\t- content: {data}')
