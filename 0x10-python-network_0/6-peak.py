#!/usr/bin/python3
"""
6-peak module
Contains find_peak function
"""


def find_peak(my_list):
    """ Finds a peak element in a list of integers """
    if not my_list or not isinstance(my_list, list):
        return None
    peak = my_list[0]
    for x in my_list:
        if x > peak:
            peak = x
        elif x < peak:
            break
    return peak
