#!/usr/bin/python3
"""A class Square with size and method of area"""


class Square:
    """Class - Square"""

    def __init__(self, size=0):
        """Square with size contructor"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area of the Square"""

        return (self.__size ** 2)
