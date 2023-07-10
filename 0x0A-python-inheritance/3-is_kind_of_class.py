#!/usr/bin/python3
""" Module 3-is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """ Returns True if obj is an instance of a_class
    or an instance of a subclass of a_class
    """
    return isinstance(obj, a_class)
