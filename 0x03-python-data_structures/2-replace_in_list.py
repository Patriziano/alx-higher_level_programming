#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    length_of_list = len(my_list)
    last_list_index = length_of_list - 1

    if idx < 0 or idx > last_list_index:
        return my_list
    else:
        my_list[idx] = element
        return my_list
