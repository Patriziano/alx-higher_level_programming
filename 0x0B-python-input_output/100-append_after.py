#!/usr/bin/python3
"""Inserts and update module"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line
    containing a specific string

    Args:
        filename: the name of the file
        search_string: the string to search for
        New_string: the new string to be generated after appending
    """
    if not filename:
        return

    with open(filename, 'r', encoding="utf-8") as f:
        read_text = f.readlines()

    with open(filename, 'w', encoding="utf-8") as f:
        for i in read_text:
            f.write(i)
            if search_string in i:
                f.write(new_string + "\n")
