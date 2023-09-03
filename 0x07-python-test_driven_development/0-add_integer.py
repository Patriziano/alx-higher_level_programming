#!/usr/bin/python3
"""This is a function that performs integere addition"""


def add_integer(a, b=98):
    """
    Add two integers

    Args:
        a (int): first integer
        b (int): second integer

    Return:
        sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return int(a + b)
