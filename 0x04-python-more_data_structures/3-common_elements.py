#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = set()
    if isinstance(set_1, set) and isinstance(set_2, set):
        common_set = set_1 & set_2
    return common_set
