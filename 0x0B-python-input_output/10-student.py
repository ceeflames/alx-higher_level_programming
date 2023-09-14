#!/usr/bin/python3
"""A Student class"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """initializes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dictionary reprentation of the student"""

        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__
