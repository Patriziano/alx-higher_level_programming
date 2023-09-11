#!/usr/bin/python3
"""Lookup case"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    Args:
        obj: The object to inspect.

    Returns:
        A list representing the attributes and methods of the object.
    """
    return dir(obj)
