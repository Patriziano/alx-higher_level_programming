#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = set()
    total = 0

    for num in my_list:
        if num not in unique:
            unique.add(num)
            total += num
    return total
