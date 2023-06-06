#!/usr/bin/python3
# Prints a string in uppercase
def uppercase(str):
    str_copy = ""
    for c in str:
        if c.islower():
            str_copy = f"{str_copy}{(chr(ord(c) - 32))}"
        else:
            str_copy = f"{str_copy}{c}"
    print("{}".format(str_copy))
