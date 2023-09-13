#!/usr/bin/python3
"""Writes a string to a textfile"""


def write_file(filename="", text=""):
    """
    returns the text written to a file
    Args:
        filename(txt): name of the testfile
        text: text to be written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        char_written = f.write(text)
        return char_written
