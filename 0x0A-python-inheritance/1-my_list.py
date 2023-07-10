#!/usr/bin/python3
""" Module 1-my_list """


class MyList(list):
    """ Defines a specialised list object """

    def print_sorted(self):
        """ Prints the list in sorted order """
        print(sorted(self))
