#!/usr/bin/python3
"""A function  returns True if the object is an exact instance of a class"""


def is_same_class(obj, a_class):
    """
    Checks if the object is exactly an instance of the specified class.

    Args:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
