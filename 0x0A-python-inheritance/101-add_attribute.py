#!/usr/bin/python3
""" Module 101-add_attribute """


def add_attribute(obj, attribute, attr_value):
    """ Adds or Sets an attribute to an object
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, attr_value)
