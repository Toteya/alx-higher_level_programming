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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes a the list of Base objects `list_obj` to
        a file
        """
        filename = f"{cls.__name__}.json"
        list_dicts = [obj.to_dictionary() for obj in list_obj]
        json_dicts = to_json_string(list_dicts)
        with open(filename, mode="w", encoding="uttf-8") as a_file:
            json.dumps(a_file, json_dicts)
