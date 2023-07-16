#!/usr/bin/python3
""" The base module
Contains Base class
"""
import json


class Base:
    """ Base class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of the given
        list of dictionaries `list_dictionaries`
        """
        if list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)
