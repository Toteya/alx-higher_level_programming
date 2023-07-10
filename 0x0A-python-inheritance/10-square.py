#!/usr/bin/python3
""" Module 10-square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines a Square object/shape
    inherits Rectangle class
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Returns the area of the Square instance """
        return self.__size ** 2
