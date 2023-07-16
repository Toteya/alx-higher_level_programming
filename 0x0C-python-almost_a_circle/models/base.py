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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of the given
        list of dictionaries `list_dictionaries`
        """
        if list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation given
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes a the list of Base objects `list_obj` to
        a file
        """
        filename = f"{cls.__name__}.json"
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_dicts = cls.to_json_string(list_dicts)
        with open(filename, mode="w", encoding="utf-8") as a_file:
            a_file.write(json_dicts)
