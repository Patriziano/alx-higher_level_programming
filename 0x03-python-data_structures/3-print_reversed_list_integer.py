#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    length_of_list = len(my_list)
    for i in range(length_of_list):
        print("{:d}".format(my_list[i]))
