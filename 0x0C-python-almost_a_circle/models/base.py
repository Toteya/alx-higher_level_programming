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

    @classmethod
    def create(cls, **dictionary):
        """ Creates and returns an instance with all attributes
        already set
        """
        if cls.__name__ == 'Rectangle':
            obj = cls(1, 1)
        elif cls.__name__ == 'Square':
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances from a file as determined by
        the file to load depends on the class e.g. Rectangle.json
        i.e. filename == <Class name>.json
        """
        filename = f"{cls.__name__}.json"
        dict_list = []
        obj_list = []
        with open(filename, mode="r", encoding="utf-8") as a_file:
            json_list = a_file.read()
            dict_list = json.loads(json_list)
            obj_list = [cls(**obj_dict) for obj_dict in dict_list]
        return obj_list

    # @classmethod

