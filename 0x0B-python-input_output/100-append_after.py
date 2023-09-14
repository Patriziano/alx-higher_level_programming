#!/usr/bin/python3
"""Inserts and update module"""


def append_after(filename="", search_string="", new_string=""):
    if not filename:
        return

    with open(filename, 'r') as f:
        read_text = f.readline()

    with open(filename, 'w') as f:
        for i in read_text:
            f.write(i)
            if search_string in i:
                f.write(new_string + "\n")
