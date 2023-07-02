#!/usr/bin/python3
""" Module 2-matrix_divided """


def matrix_divided(matrix, div):
    """Divides all the elements of a matrix by a number

    Args:
        matrix (obj:`list` of obj:`list` of int or float): The matrix to be
            divided
        div (int or float): The number to divide the matrix by

    Returns:
        A new matrix, with elements rounded to 2 decimal places if successful
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if any(not isinstance(a_list, list) for a_list in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    list_len = len(matrix[0])
    new_matrix = []
    for a_list in matrix:
        if any(not isinstance(x, (int, float)) for x in a_list):
            raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
        if list_len != len(a_list):
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([round(x/div, 2) for x in a_list])
    return new_matrix
