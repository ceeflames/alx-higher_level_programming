#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """ Appends a string to the end of a text file (UTF-8 encoded)"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
