#!/usr/bin/python3
"""Area of the BaseGeometry"""


class BaseGeometry:
    """
    A base class for geometry-related operations.

    This class can be used as a foundation for defining
    various geometry classes and methods.
    """

    def area(self):
        """
        Calculate the area of the geometry shape.

        Raises:
        NotImplementedError: This method must be implemented inderived
        classes.
        """
        raise NotImplementedError("area() is not implemented")
