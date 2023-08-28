#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return (0)
    count = 0
    try:

        for elements in range(x):
            if count < x:
                print("{}" format.my_list(element), end=" ")
                count += 1

        print()
    except:
        pass
    return (count)
