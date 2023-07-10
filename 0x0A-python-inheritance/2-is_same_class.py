#!/usr/bin/python3
""" Module 2-is_same_class """


def is_same_class(obj, a_class):
    """ Returns true if obj is exactly an instance of a_class
    """
    # return obj.__class__ == a_class
    return type(obj) is a_class
