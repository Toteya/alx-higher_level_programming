#!/usr/bin/python3
""" Module 5-save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file using JSON
    representation
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
