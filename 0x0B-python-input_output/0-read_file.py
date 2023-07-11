#!/usr/bin/python3
""" Module 0-read_file.py """


def read_file(filename=""):
    """ Reads the contents of a file and prints to stdout
    """
    with open(filename, encoding="utf-8") as a_file:
        text = a_file.read()
        print(text, end="")
