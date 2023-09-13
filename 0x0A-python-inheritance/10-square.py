#!/usr/bin/python3
"""A sqaure class that inherits fromparent class Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from superclass rectangle"""
    def __init__(self, size):
        """Initializer"""
        self.__size = size

        self.integer_validator("size", size)

    def area(self):
        """Area of the square"""
        area = self.__size * self.__size
        return area

    def __str__(self):
        return ("[{}] {}/{}".format(
            "Rectangle", self.__size, self.__size))
