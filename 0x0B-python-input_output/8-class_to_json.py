#!/usr/bin/python3
""" 8-class_to_json module """
import json


def class_to_json(obj):
    """ Returns the dictionary discription for JSON
    serialization of an object
    """
    return json.dumps(obj.__dict__)
