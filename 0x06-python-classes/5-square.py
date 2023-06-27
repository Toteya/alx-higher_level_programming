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

    def my_print(self):
        """Prints the square as # depending on the size"""
        for i in range(self.size):
            print("#" * self.size)
        if not self.size:
            print()
