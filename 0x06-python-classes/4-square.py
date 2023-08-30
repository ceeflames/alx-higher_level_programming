#!/usr/bin/python3
"""Class Square with size, area, getter and setters"""


class Square:
    """Class - Square"""

    def __init__(self, size=0):
        """Square with constructor"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Area of the Square method"""
        return (self.__size ** 2)


    @property
    def size(self):
        """Getter of the private attb size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for the size private attb size"""
        if (type(value) is not int):
            raise (TypeError("size must be an integer"))
        if value < 0:
            raise (ValueError("size must be >= 0"))

            self.__size = value
