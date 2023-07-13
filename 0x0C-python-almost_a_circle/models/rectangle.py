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

    @property
    def width(self):
        """ The width of the Rectangle instance
        """
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """ The height of the Rectangle instance
        """
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def x(self):
        """ x """
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        """ y """
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y
