#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    length_of_list = len(my_list)
#    last_list = length_of_list - 1
    for i in range(length_of_list - 1, -1, -1):
        print("{:d}".format(my_list[i]))
