#!/usr/bin/python3
""" rectangle module
Contains the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle class
    inherits the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate_int(self, name, value):
        """ Validates the datatype of the variable.
        Must be an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

    def validate_gt_zero(self, name, value):
        """ Validates the value of the variable.
        Must be greater than zero.
        """
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def validate_ge_zero(self, name, value):
        """ Validates the value of the variable.
        Must be greater or equal to zero.
        """
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """ The width of the Rectangle instance
        The width must be a positive integer
        """
        return self.__width

    @width.setter
    def width(self, width):
        self.validate_int("width", width)
        self.validate_gt_zero("width", width)
        self.__width = width

    @property
    def height(self):
        """ The height of the Rectangle instance
        The height must be a positive integer
        """
        return self.__height

    @height.setter
    def height(self, height):
        self.validate_int("height", height)
        self.validate_gt_zero("height", height)
        self.__height = height

    @property
    def x(self):
        """ x
        x must be an integer greater or equal to zero.
        """
        return self.__x

    @x.setter
    def x(self, x):
        self.validate_int("x", x)
        self.validate_ge_zero("x", x)
        self.__x = x

    @property
    def y(self):
        """ y
        y must be an integer greater or equal to zero.
        """
        return self.__y

    @y.setter
    def y(self, y):
        self.validate_int("y", y)
        self.validate_ge_zero("y", y)
        self.__y = y

    def area(self):
        """ Returns the area of the Rectangle instance
        """
        return self.width * self.height
