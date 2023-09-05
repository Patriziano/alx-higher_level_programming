#!/usr/bin/python3
""" a function that prints the user's full name"""


def say_my_name(first_name, last_name=""):
    """
    Prints the full name with the given first and last names.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name (default is an empty string).

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if first_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(last_name))
