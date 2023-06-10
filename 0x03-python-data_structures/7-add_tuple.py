#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n_list = []
    for i in range(2):
        a, b = 0, 0
        if i < len(tuple_a):
            a = tuple_a[i]
        if i < len(tuple_b):
            b = tuple_b[i]
        n_list.append(a + b)
    return tuple(n_list)
