#!/usr/bin/python3
""" Module 100-my_int """


class MyInt(int):
    """ MyInt is an integer with strange characteristics
    It has == and != operators inverted
    """

    def __ne__(self, other):
        """ Returns True if self is equal to other (inverted)
        """
        return self.real == other

    def __eq__(self, other):
        """ Returns True if self is not equal to other (inverted)
        """
        return self.real != other
