#!/usr/bin/python3
""" 1-write_file module """


def write_file(filename="", text=""):
    """ Writes text to a file
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
