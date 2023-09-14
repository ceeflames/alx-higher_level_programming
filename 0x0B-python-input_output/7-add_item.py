#!/usr/bin/python3
"""scripts that adds all arguments to a python list"""


import json
import sys
from os.path import exists


def add_arguments_to_list(argc_list, arg):
    argc_list.append(arg)

def main():

    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
            __import__('6-load_from_json_file').load_from_json_file

    if exists("add_item.json"):
        items = load_from_json_file("add_item.json")
    else:
        items = []

    for arg in sys.argv[1:]:
        add_arguments_to_list(items, arg)

        save_to_json_file(items, "add_item.json")

if __name__ == "__main__":
    main()
