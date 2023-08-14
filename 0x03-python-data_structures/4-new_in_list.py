#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_of_list = list(my_list)
    if idx < 0 or idx >= (len(my_list)):
        return copy_of_list
    else:
        copy_of_list[idx] = element
        return copy_of_list 
