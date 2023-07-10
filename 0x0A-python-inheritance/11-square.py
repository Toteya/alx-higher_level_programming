#!/usr/bin/python3
""" Module 11-square """
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

    def __str__(self):
        """ Returns a string representation of the Square instance
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
