#!/usr/bin/python3
for num in range(122, 96, -1):
#    conv = chr(num)
    if num % 2 == 0:
        char = chr(num).lower()
    else:
        char = chr(num).upper()
    print("{}".format(char), end="")
