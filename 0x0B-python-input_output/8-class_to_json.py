#!/usr/bin/python3
""" Module 8-class_to_json module
"""


def class_to_json(obj):
    """ Returns the dictionary discription for JSON
    serialization of an object
    """
    return obj.__dict__
