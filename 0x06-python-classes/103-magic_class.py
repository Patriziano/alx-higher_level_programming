#!/usr/bin/python3
"""MagicClass bytecode disassemble"""


from math import pi


class MagicClass:
    """MagicCode bytecode disassemble"""

    def __init__(self, radius=0):
        """
        Initializing the MagicCode with a given radius at 0

        Args:
            radius(int): radius must be integer or float
        Raises:
            TypeError: if radius is not a number
        """

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        calculates the area

        Returns:
            the calculated area
        """
        return self.__radius ** 2 * pi

    def circumference(self):
        """
        Calculates the circumference of the MagicClass

        Returns:
        The circumference of the class
         """
        return 2 * pi * self.__radius
