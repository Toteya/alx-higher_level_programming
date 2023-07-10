#!/usr/bin/python3
""" Module 9-rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines a Rectangle
    subclass of BaseGeometry
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of the Rectangle instance
        """
        return self.__width * self.__height

    def __str__(self):
        """ Returns a string representation of the Rectangle instance
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
