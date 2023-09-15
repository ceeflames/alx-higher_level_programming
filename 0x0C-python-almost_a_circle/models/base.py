#!/usr/bin/python3
"""First class base"""


class Base:
    """ private class attribute """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            """ assign the public instance attr id with the argument value"""
            self.id = id
        else:
            """ increment __nb_object and assign the new value to id """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
