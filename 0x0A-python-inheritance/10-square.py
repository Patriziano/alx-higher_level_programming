#!/usr/bin/python3
"""A class Rectangle"""


class BaseGeometry:
    """
    A base class for geometry-related operations.

    This class can be used as a foundation for defining various
    geometry classes and methods.
    """

    def area(self):
        """
        Calculate the area of the geometry shape.

        Raises:
        Exception: This method should be implemented in derived classes.
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that 'value' is an integer greater than 0.

        Args:
        name (str): The name of the value being validated.
        value (int): The value to be validated.

        Raises:
        TypeError: If 'value' is not an integer.
        ValueError: If 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
    __width (int): The width of the rectangle.
    __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle object with specified width and height.

        Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.

        Raises:
        TypeError: If 'width' or 'height' is not an integer.
        ValueError: If 'width' or 'height' is less than or equal to 0.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

    def area(self):
        """
        Implements the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Prints the string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """The Square class that inherits from the Rectangle"""
    def __init__(self, size):
        """
        Initializes a square class with specified size

        Args:
            size(int): size of the square
        """
        super().__init__(size, size)
