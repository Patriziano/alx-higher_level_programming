#!/usr/bin/python3
"""A class square"""


class Square:
    """
    A class square that defines a square with private instance size
    """
    def __init__(self, size):
        """
        Initializes an instance of the square class with a given size

        Args:
            size (int): size of the square

        """
        self.__size = size
