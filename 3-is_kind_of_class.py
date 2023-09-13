#!/usr/bin/python3
""" is_kind_of_class method """


def is_kind_of_class(obj, a_class):
    """ checks the obj type """

    if not isinstamce(obj, a_class):
        return False
    else:
        return True
