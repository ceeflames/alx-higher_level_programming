#!/usr/bin/python3
"""
    Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as status:
        content = status.read()
        print("Body response:")
        print(f'\t- type: {type(content)}')
        print(f'\t- content: {content}')
        print(f'\t- utf8 content: {content.decode("utf-8")}')
