#!/usr/bin/python3
import math
class Circle:

    def __init__(self, radius=0):
        self.radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__area = math.pi * (radius ** 2)
        self.__radius = radius

    @property
    def area(self):
        return self.__area

my_circle = Circle(3)
print(f"Radius: {my_circle.radius}")
print(f"Area: {my_circle.area}")
my_circle.radius = 2
print(f"Radius: {my_circle.radius}")
print(f"Area: {my_circle.area}")
