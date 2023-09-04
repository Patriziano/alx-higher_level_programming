#!/usr/bin/python3
"""a class Rectangle that defines a rectangle"""


class Rectangle:
    """
    A class that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the instance of the class with width and height

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        Raises:
            TypeError: if width is not an int
                        if height is not an int

            ValueError: if width is less than 0
                        if height is less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the width the triangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Sets the width of the rectangle

        Args:
            value (int):  value to set it to
        Raises:
            TypeError: if width is not an int
             ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Get height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle

        Args:
            value (int): value to set it to
        Raises:
            TypeError: if width is not an int
            ValueError: if width is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """
        returns the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * ((self.width + self.height))

    def __str__(self):
        """
        print the rectangle with the character #
        """

        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += "#" * self.width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """
         should return a string representation of the rectangle
         """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
