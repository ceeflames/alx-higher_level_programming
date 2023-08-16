#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    num = set()
    for i in my_list:
            if i not in num:
                res += i
                num.add(i)
    return (res)
