#!/usr/bin/python3
# Prints the last digit of a number
def print_last_digit(number):
    a = str(int(number))
    b = a[-1]
    print("{}".format(b), end="")
    return b
