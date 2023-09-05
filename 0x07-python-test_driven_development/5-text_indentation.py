#!/usr/bin/python3
"""
Module composed by a function that prints atext with e lines
"""
def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters
    text: input string
    returns: no return
    raises: TypeError
    """
    if type(text) not in (str):
        raise TypeError("text must be a string")

    new_line = True

    for char in text:
        if char in ('.', '?', ':'):
            print(char, end="")
            print("\n" * 2, end="")
            new_line = True

        else:
            if new_line:
                print()
                new_line = False
            print(char, end="")
