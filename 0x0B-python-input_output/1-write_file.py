#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    with open(filename, 'w', ebcoding="utf-8") as f:
        writt_en = file.write(text)

    return writt_en
