#!/usr/bin/python3
"""The Square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class that is inherited from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """The constructor that initializes the Square class instances"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        square = '[Square] '
        square_id = "({}) ".format(self.id)
        square_para = "{}/{} ".format(self.x, self.y)
        square_size = "{}".format(self.width)
        return square + square_id + square_para + "- " + square_size

    @property
    def size(self):
        """The getter function for size"""
        return self.width

    @size.setter
    def size(self, value):
        """The setter function"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes using positional and keyword arguments."""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
