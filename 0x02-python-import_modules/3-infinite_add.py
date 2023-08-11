#!/usr/bin/python3

if __name__ == '__main__':

    from sys import argv

    args = argv[1:]
    output = 0

    for arg in args:
        num_arg = int(arg)
        output += num_arg

    print(output)
