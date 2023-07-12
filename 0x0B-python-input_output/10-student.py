#!/usr/bin/python3
""" Module 10-student """


class Student:
    """ class Student """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns a dictionary representation of this
        Student instance of the given attributes `attrs`
        """
        if not attrs:
            return self.__dict__
        dict = {}
        for key in attrs:
            if key in self.__dict__:
                dict.update({key: self.__dict__.get(key)})
        return dict
