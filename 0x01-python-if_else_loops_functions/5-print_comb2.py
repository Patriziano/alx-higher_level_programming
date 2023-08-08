#!/usr/bin/python3
for num in range(0, 99+1):
    print("{:02d}".format(num), end=", " if num < 99 else "\n")
