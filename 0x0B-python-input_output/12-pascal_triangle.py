#!/usr/bin/python3
""" Module 12-pascal_triangle """


def pascal_triangle(n):
    """ Generates a pascals triangle of size n
    Returns:
        A list of lists representing pascals triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    for i in range(n):
        level = []
        level.append(1)
        for j in range(i):
            try:
                level.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
            except IndexError:
                level.append(triangle[i - 1][j])
        triangle.append(level)
    return triangle
