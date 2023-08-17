#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)

    score = 0
    weight = 0

    for key, value in my_list:
        score += key * value
        weight += value

    if weight == 0:
        return (0)

    ave = score / weight
    return (ave)
