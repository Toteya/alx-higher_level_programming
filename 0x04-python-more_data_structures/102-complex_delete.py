#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return None
    while value in a_dictionary.values():
        try:
            idx = list(a_dictionary.values()).index(value)
            key = list(a_dictionary.keys())[idx]
            del a_dictionary[key]
        except KeyError:
            break
    return a_dictionary
