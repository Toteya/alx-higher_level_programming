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

    def update(self, *args, **kwargs):
        """ Updates the Rectangle instance attributes
        arg 1: id
        arg 2: size
        arg 3: x
        arg 4: y
        """
        if len(args) == 0:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if hasattr(self, key):
                        setattr(self, key, value)
                    else:
                        raise AttributeError("'Square' \
object has no attribute '{key}'")
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """ Returns a dictionary representation of the Square
        """
        _dict = {key.split("_")[-1]: value for key, value in
                 self.__dict__.items()}
        _dict['size'] = _dict['width']
        del _dict['width']
        del _dict['height']
        return _dict
