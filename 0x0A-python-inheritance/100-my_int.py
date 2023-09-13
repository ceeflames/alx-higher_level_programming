#!/usr/bin/python3
"""A MyInt class that inherits from int"""


class MyInt(int):
    """operators"""
    def __eq__(self, value):
        """Using the magic method of Equal Override the == operator with !="""
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
