#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    biggest_key = None
    biggest_integer = max(a_dictionary.keys())
    for key, value in a_dictionary.items():
        if value == biggest_integer:
            biggest_key = key
            break
    return biggest_integer
