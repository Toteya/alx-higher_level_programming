#!/usr/bin/python3
""" Module 7-base_geometry
Contains empty class BaseGeometry
"""


class BaseGeometry:
    """ Defines a Geometry object """

    def area(self):
        """ returns the area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates the value """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
