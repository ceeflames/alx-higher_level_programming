#!/usr/bin/python3
"""
   Module run by a function that adds 2 integers
"""
def add_integer(a, b=98):
    """
    funtion that adds two int and converts floats to int

    adds a and b

    Returns: the sum of a and b

    Raise TypeError: if a or b is not integer

    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return (a + b)
