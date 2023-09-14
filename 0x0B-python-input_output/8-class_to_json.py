#!/usr/bin/python3
"""function that returns the dictionary description with simeple data structure"""


def class_to_json(obj):
    """Returns the dictionary description"""
    return obj.__dict__
