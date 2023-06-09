#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for x in my_list:
        print("{}".format(x))
    # Alternative Approach:
    # print(*my_list, sep="\n")
