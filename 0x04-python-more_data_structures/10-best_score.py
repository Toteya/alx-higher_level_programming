#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        values = list(a_dictionary.values())
        keys = list(a_dictionary.keys())
        top_score = max(values)
        return keys[values.index(top_score)]
