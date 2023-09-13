#!/usr/bin/python3
"""Function that adds a new attribute to an object"""


def add_attribute(self, name, value):
    """add attribute"""
    if hasattr(self, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(self, name, value)
