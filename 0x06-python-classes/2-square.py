#!/usr/bin/python3
"""A class square"""


class Square:
    """
    A class square that defines a square with private instance size
    """
    def __init__(self, size=0):
        """
        Initializes an instance of the square class with a given size to 0

        Args:
            size (int): size of the square

        Raise:
            TypeError: If size is not integer
            ValueError: if size is less than 0

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
