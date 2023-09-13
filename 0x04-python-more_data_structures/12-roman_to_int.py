#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    dic = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    result = dic[roman_string[0]]

    for i in range(0, len(roman_string) - 1):
        if dic[roman_string[i]] >= dic[roman_string[i + 1]]:
            result = result + dic[roman_string[i + 1]]
        else:
            result = dic[roman_string[i + 1]] - result

    return result
