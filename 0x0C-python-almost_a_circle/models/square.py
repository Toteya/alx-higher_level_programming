#!/usr/bin/python3
""" square module """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ defines a Square object
    subclass of Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Returns the size (width) of the Square instance
        Setter method raise a TypeError if size is not an integer,
        and a ValueError exception if size is not greater than 0.
        """
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        """ Returns a string representation of the
        Square object
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
