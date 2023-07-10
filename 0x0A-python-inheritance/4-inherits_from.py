#!/usr/bin/python3
""" Module 4-inherits_from """


def inherits_from(obj, a_class):
    """ Returns True if the class of obj inherits from a_class """
    if not isinstance(a_class, type):
        return False
    return type(obj) is not a_class and issubclass(obj.__class__, a_class)
