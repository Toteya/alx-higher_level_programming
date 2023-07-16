#!/usr/bin/python3
"""This module defines the Square class"""


class Square():
    """This class defines a square and its attributes"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialises an instance of Square

        Args:
            size (int, optional): The initial size of the Square instance.
                Defaults to 0. Must be >= 0
            posititon (tuple, optional): The position of square to be printed
        """
        self.size = size
        self.position = position

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        """int: The size of the Square instance

        Setter raises TypeError if size is not an int, and ValueError if
        size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """tuple: The position of the square to be printed on the screen

        Setter raises TypeError if position is not a tuple and does not contain
        two positive integers.
        """
        return self.__position

    @position.setter
    def position(self, position):
        if isinstance(position, tuple) and len(position) == 2:
            if all(isinstance(x, int) for x in position):
                if all(x >= 0 for x in position):
                    self.__position = position
                    return
        raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """Prints the square as # depending on the size"""
        if not self.size:
            print()
        else:
            print('\n' * self.position[1], end="")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
