#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    #diff_element = {x for x in set_1 if x not in set_2}
    diff_element = set_1 ^ set_2
    return diff_element
