#!/usr/bin/python3
"""The Rectangle class module"""

from models.base import Base


class Rectangle(Base):
    """The Rectangle class inheriting from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor that initializes the instances of the class Rectangle

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate
            y (int): The y coordinate
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter function"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height getter function"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x coordinate getter function"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter function"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter function"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter function"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """computes the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout rectangle instance with #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """__str__ method"""
        rect = "[Rectangle] "
        rect_id = "({}) ".format(self.id)
        rect_cord = "{}/{} ".format(self.x, self.y)
        rect_para = "{}/{}".format(self.width, self.height)
        return rect + rect_id + rect_cord + "- " + rect_para

    def update(self, *args, **kwargs):
        """Update attributes using positional and keyword arguments."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """Rectangle instance to dictionary representation"""
        dict_rep = {}
        list_attr = ['id', 'width', 'height', 'x', 'y']
        for key in list_attr:
            dict_rep[key] = getattr(self, key)
        return dict_rep
