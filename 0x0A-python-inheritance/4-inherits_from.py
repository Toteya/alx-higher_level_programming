#!/usr/bin/python3
""" Module 4-inherits_from """


def inherits_from(obj, a_class):
    """ Returns True if the class of obj inherits from a_class """
    return issubclass(type(obj), a_class)
