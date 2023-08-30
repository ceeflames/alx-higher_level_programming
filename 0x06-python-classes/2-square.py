#!/usr/bin/python3

"""Square: Define a square"""


class Square:

    """
    Square: A class square

    size: size of the square
    """


    def __init__(self, size=0):
        """Square with size constructor"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
         self.__size = size
