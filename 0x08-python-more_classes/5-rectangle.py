#!/usr/bin/python3
""" 0-rectangle module """


class Rectangle:
    """ Class Rectangle defines a rectangle """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ The width of the rectangle

        width must be an int, otherwise TypeError is raised
        width must be >= 0
        """
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """ The height of the rectangle

        height must be an integer, and must be >= 0
        """
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """ Returns the area of the rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ Returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ Returns a rectangle with '#' characters """
        if self.__width == 0 or self.__height == 0:
            return ""
        row = '#' * self.__width
        rectangle_str = (row + '\n') * self.__height
        rectangle_str = rectangle_str[:-1]  # Remove the last newline character
        return rectangle_str

    def __repr__(self):
        """ Returns the string represantation of the recatangle """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Called when this Rectangle instance is deleted """
        print("Bye rectangle...")
