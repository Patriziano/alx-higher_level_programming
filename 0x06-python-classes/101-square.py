#!/usr/bin/python3
"""A class square"""


class Square:
    """
    A class square that defines a square with private instance size
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes an instance of the square class with a given size to 0

        Args:
            size (int): size of the square

        Raise:
            TypeError: If size is not integer
            ValueError: if size is less than 0

        """
        self.size = size
        self.position = position

    def area(self):
        """
        Public instance method that returns the current square area

        Returns:
            current square area
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdout the square with the character #

        prints a empty line if size = 0
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    @property
    def position(self):
        """
        Gets the position of the square

        Returns:
             tuple: a tuple of 2 positive integers(position)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method to set the position of the square.

        Args:
            value (tuple): The new position value to set.

        Raises:
            TypeError: If value is not a tuple with 2 integers.
            ValueError: If position values are less than 0.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(val, int) for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(val < 0 for val in value):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """
            Getter - To retrieve the data

            Returns:
                Retrieved data
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter - To change the data

        Args:
            Value(int): The value to be set to
        Returns:
            The changed data.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __str__(self):
        """
        Printing a string representation of the square (same as my_print).

        Returns:
            str: A string printing the square.
        """
        if self.__size == 0:
            return ""

        result = ""
        for _ in range(self.__position[1]):
            result += "\n"

        for _ in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size + "\n"

        return result.rstrip()
