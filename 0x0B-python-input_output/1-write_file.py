#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """write text in filename with utf-8"""
    with open(filename, 'w', ebcoding="utf-8") as f:
        writt_en = f.write(text)

    return writt_en
