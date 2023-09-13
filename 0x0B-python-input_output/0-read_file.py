#!/usr/bin/python3
"""read a textfile to stdout"""


def read_file(filename=""):
    """
    reads a textfile to stdout

    Args:
        filename (txt): The name of the file to read
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        for line in read_data:
            print(line, end="")
