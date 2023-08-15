#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length_of_list = len(my_list)
    new_list = []
    if idx < 0 or idx >= length_of_list:
        return my_list
    for i in range(length_of_list):
        if i != idx:
            new_list.append(my_list[i])
    del my_list[idx]
    return new_list
    
