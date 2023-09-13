#!/usr/bin/python3
"""function that returns an object"""


import json


def from_json_string(my_str):
    """Returns a python data structure represented by a JSON"""
    return json.loads(my_str)
