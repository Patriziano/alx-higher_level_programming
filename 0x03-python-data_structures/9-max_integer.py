#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is not None:
        big_num = my_list[0]
        for i in my_list:
            if i > big_num:
                big_num = i
        return big_num
