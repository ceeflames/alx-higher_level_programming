#!/usr/bin/python3
def uppercase(str):
    n = ""
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            n = n + chr(ord(str[i]) - 32)
        else:
            n = n + str[i]
    print("{}".format(n))
