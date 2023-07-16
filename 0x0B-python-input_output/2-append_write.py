#!/usr/bin/python3
""" Module 2-append_write """


def append_write(filename="", text=""):
    """ Appends text to a file
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
