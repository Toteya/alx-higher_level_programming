#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = ""
    i = 0
    for c in str:
        if i != n:
            str_copy += c
        i += 1
    return (str_copy)
