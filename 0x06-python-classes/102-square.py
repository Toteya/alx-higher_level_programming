#!/usr/bin/python3
"""This module defines the Square class"""


class Square():
    """This class defines a square and its attributes"""

    def __init__(self, size=0):
        """Initialises an instance of Square

        Args:
            size (int): The initial size of the Square instance; must be >= 0
        """
        self.size = size

    def area(self):
        """Returns the area of the square (size^2)"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter method for the __size attribute"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter method for the __size attribute"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def __eq__(self, other):
        """ Compares the size of this Square instance to `other`
        Returns True if the sizes of the two squares are equal
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.area() == other.area()

    def __lt__(self, other):
        """ Returns True if the size of this Square instance is less than
        `other`
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        """ Returns True if the size of this Square instance is less than
        or equal to `other`
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.area() <= other.area()

    def __gt__(self, other):
        """ Returns True if the size of this Square instance is greater than
        `other`
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        """ Returns True if the size of this Square instance is greater than
        or equal to `other`
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.area() >= other.area()

    def __ne__(self, other):
        """ Returns True if the size of this Square instance is not
        equal to `other`
        """
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.area() != other.area()
