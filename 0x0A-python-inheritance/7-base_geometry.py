#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """An empty attribute"""

    def area(self):
        """raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check for the value"""
        self.name = name
        self.value = value

        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
