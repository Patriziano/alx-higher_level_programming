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
        self.__size = size

    def area(self):
        """
        Public instance method that returns the current square area

        Returns:
            current square area
        """
        return self.__size ** 2

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

    def __eq__(self, other):
        """Equality comparator"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comparator"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparator"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparator"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Less than comparator"""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparator"""
        return self.area() <= other.area()
