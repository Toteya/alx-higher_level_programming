#!/usr/bin/python3
""" 0-rectangle module """


class Rectangle:
    """ Class Rectangle defines a rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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
        row = str(self.print_symbol) * self.__width
        rect_str = (row + '\n') * self.__height
        rect_str = rect_str[:-1]  # Remove the last newline character
        return rect_str

    def __repr__(self):
        """ Returns the string represantation of the recatangle """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Called when this Rectangle instance is deleted """
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares two rectanglees and returns the biggest
        of the two rectangles based on their areas

        Args:
            rect_1 (obj: `Rectangle`): The first rectangle
            rect_2 (obj: `Rectangle`): The second rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ Instantiates a new Rectangle object

        Args:
            size (int): Size of the rectangle (width, height = size)
        """
        return cls(size, size)
