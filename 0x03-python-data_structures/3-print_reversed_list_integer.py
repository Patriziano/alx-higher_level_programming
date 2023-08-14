#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        length_of_list = len(my_list)
        rev_list = my_list[length_of_list-1::-1]
        for i in rev_list:
            print("{:d}".format(i))
