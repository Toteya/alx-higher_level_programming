#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in sorted(iter(a_dictionary)):
        print(f"{key}: {a_dictionary[key]}")
