#!/usr/bin/python3
"""Appends a string to a file module"""


def append_write(filename="", text=""):
    """
    appends a string to a textfile
    Args:
        filename (txt): name of the file
        text(str): the string to be added
    Returns:
        Number of character added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        append_string = f.write(text)
        return append_string
