#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key = list(a_dictionary.keys())[0]
    for k in a_dictionary:
        if a_dictionary[k] > a_dictionary[key]:
            key = k
    return key
