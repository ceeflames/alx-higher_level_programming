#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value == None:
        return (a_dictionary)
    del_key = []

    for key, values in a_dictionary.items():
        if values == value:
            del_key.append(key)

    for key in del_key:
        a_dictionary.pop(key, None)
