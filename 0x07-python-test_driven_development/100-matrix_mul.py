#!/usr/bin/python3
""" Module 100-matrix_mul multiplies two
matrices
"""


def matrix_mul(m_a, m_b):
    """ Multiplies two matrices and returns a
    new matrix of the products of the elements
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # every list (element) in the matrix is a row
    if any(not isinstance(a_list, list) for a_list in m_a):
        raise TypeError("m_a must be a list of lists")
    if any(not isinstance(b_list, list) for b_list in m_b):
        raise TypeError("m_b must be a list of lists")
    if any(len(a_list) == 0 for a_list in m_a):
        raise ValueError("m_a can't be empty")
    if any(len(b_list) == 0 for b_list in m_b):
        raise ValueError("m_b can't be empty")
    if any(len(a_list) != len(m_a[0]) for a_list in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(b_list) != len(m_b[0]) for b_list in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # number of columns of m_a must be equal to the number of rows of m_b
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    for a_list in m_a:
        if any(not isinstance(x, (int, float)) for x in a_list):
            raise TypeError("m_a should contain only integers or floats")
    for b_list in m_b:
        if any(not isinstance(y, (int, float)) for y in b_list):
            raise TypeError("m_b should contain only integers or floats")

    m_new = []
    for a_list in m_a:
        r_list = []
        for i in range(len(m_b[0])):
            x = 0
            for j in range(len(a_list)):
                x += a_list[j] * m_b[j][i]
            r_list.append(x)
        m_new.append(r_list)
    return m_new
