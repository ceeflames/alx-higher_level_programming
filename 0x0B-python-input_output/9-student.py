#!/usr/bin/python3
"""A student class"""


class Student:
    """student"""
    def __init__(self, first_name, last_name, age):
        """initializer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Student instance in a dictionatry"""
        return self.__dict__
