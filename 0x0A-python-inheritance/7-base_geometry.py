#!/usr/bin/python3
"""Validator of the class"""


class BaseGeometry:
    """
    A base class for geometry-related operations.

    This class can be used as a foundation for defining various geometry classes
    and methods.
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
        Validate that a given value is an integer greater than 0.

        Args:
        name (str): The name of the value being validated.
        value (int): The value to be validated.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
