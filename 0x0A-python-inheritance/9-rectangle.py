#!/usr/bin/python3
"""A rectangle class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass of the parent clasee BaseGeometry"""
    def __init__(self, width, height):
        """initialize"""
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Area of the rectangle"""
        area = self.__width * self.__height
        return area

    def __str__(self):
        """magic method to return a string"""
        return ("[{}] {}/{}".format(
            type(self).__name__, self.__width, self.__height)
            )
