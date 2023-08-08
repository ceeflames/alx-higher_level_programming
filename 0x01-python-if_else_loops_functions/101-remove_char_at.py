#!/usr/bin/python3
def remove_char_at(str, n):
    num = ""
    for i in range(len(str)):
        if i == n:
            continue
        else:
            num = num + str[i]
    return (num)
