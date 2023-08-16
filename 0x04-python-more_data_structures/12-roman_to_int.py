#!/usr/bin/python3
def roman_to_int(roman_string):
    num = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D':500, 'M': 1000
            }
    res = 0

    if roman_string:
        element = 0
        for romans in reversed(roman_string):
            value = num.get(romans, 0)

            if value < element:
                res -= value
            else:
                res += value

            element = value
        return (res)
     
    return (None)
