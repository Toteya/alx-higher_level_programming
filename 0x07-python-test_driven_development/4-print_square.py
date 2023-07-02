#!/usr/bin/python3
""" Module: 4-print_square """


def print_square(size):
    """ Prints a square of any given size

    Args:
        size (int): The size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    line = f"{'#' * size}\n"
    print(line * size, end="")
