#!/usr/bin/python3
""" a function that prints a square with the character #"""


def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size (int): The size (length) of the square.

    Returns:
        None
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
