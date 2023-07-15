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

    def __str__(self):
        """ Returns a string representation of the
        Square object
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
