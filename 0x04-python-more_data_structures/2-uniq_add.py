#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    if my_list:
        my_set = set(my_list)
        for x in my_set:
            sum += x
    return sum
