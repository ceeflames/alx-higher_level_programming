#!/usr/bin/python3

""" 
Function on the obj instance of a class 
"""



def inherits_from(obj, a_class):
    """
        The function returns True of the obj is an  instance of a class 
        that inherited from the specified class. otherwise False
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
