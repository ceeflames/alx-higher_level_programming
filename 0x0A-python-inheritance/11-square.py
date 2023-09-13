#!/usr/bin/python3
"""A square class that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Inherits from parent class rectangle"""
    def __init__(self, size):
        """initialize"""
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """Area of the square"""
        area = self.__size * self.__size
        return area

    def __str__(self):
        """magic method for string"""
        return ("[{}] {}/{}".format(
            type(self).__name__, self.__size, self.__size)
            )
