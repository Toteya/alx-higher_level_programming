#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for x in matrix[i]:
            print("{:d}".format(x), end=" ")
        print()
