#!/usr/bin/python3
"""Function is an instance of a class"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    (directly or indirectly)from the specified class.

    Args:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    True if obj is an instance of a subclass of a_class, otherwise False.
    """
    return issubclass(type(obj), a_class)
