#!/usr/bin/python3

"""
Module composed by a function that defines a rectangle
"""
class Rectangle:
    """
    rectangle class 
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
