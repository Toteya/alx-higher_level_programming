#!/usr/bin/python3
""" Module 9-student """


class Student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns the dictionary representation of this
        Student instance
        """
        return self.__dict__
