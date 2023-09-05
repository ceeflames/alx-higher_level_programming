#!/usr/bin/python3
"""
MODULE COMPOSED BY A FUNCTION THAT PRINTS A MASSAGE
"""
def say_my_name(first_name, last_name=""):
    """
    function that prints name
    first-name, last_name

    return: no return

    raise: TypeError

    """

    if type(first_name) not in (str):
        raise TypeError ("first_name must be a string")
    if type(last_name) not in (str):
        raise TypeError ("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
