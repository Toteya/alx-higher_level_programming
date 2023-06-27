#!/usr/bin/python3
"""This module defines the Square class"""


class Square():
    """This class defines a square and its attributes"""

    def __init__(self, size=0):
        """Initialises an instance of Square

        Args:
            size (int): The initial size of the Square instance; must be >= 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size
