#!/usr/bin/python3
"""
Module composed by a function that prints a square with the charachter #
"""
def print_square(size):
    """ function that prints a square eith the character #
    size: size of the square printed
    return: no return
    raises: TypeError
    """
    if type(size) not in (int):
        raise TypeError ("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) in (float):
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end=" ")
        print()
