#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []

    for num in my_list:
        is_divisible = num % 2 == 0
        res.append(is_divisible)
    return (res)
