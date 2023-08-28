#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    counter = 0

    try:
        while i < x:
            if counter >= x:
                break

            if isinstance(my_list[counter], int):
                print("{:d}".format(my_list[counter]), end="")
                i += 1
            counter += 1
    except (TypeError, ValueError):
        pass
    print()
    return i
