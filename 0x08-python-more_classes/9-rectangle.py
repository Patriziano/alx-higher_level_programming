#!/usr/bin/python3
"""a class Rectangle that defines a rectangle"""


class Rectangle:
    """
    A class that defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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
            rectangle_str += str(self.print_symbol) * self.width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """
         should return a string representation of the rectangle
         """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        To delete an instance of the rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Static method that returns the biggest rectangle based on the area

        Args:
            rect_1 (Rectangle): value of the area
            rect_2 (Rectangle): value of the area

        Raises:
            TypeError: if rect_1 is not an instance of Rectangle
                        if rect_2 is not an instance of Rectangle
        Return:
            Biggest rectangle based on the area
            rect_1 if both have the same area value
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        first_area = rect_1.area()
        second_area = rect_2.area()

        if first_area >= second_area:
            return rect_1
        elif first_area == second_area:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        class method that returns a new Rectangle instance with
        width == height == size
        """
        return cls(size, size)
