#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_keys = [keys for keys, i in a_dictionary.items() if i == value]
    for key in delete_keys:
        del a_dictionary[key]
    return a_dictionary
