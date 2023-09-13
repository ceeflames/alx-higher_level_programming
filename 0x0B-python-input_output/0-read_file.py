#!/usr/bin/python3
"""function that reads a text file"""


def read_file(filename=""):
    """Reads and print the content of a text file to stdout"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
