#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    sym_diff = set()
    if not isinstance(set_1, set):
        sym_diff = set_2.copy()
    elif not isinstance(set_2, set):
        sym_diff = set_1.copy()
    else:
        sym_diff = set_1 ^ set_2
    return sym_diff
