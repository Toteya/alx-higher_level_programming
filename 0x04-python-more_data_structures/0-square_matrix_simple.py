#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    if matrix:
        for row in matrix:
            square_matrix.append([x**2 for x in row])
    return square_matrix
