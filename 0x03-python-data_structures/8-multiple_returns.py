#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        res = 0, None
    else:
        res = len(sentence), sentence[0]
    return (res)
