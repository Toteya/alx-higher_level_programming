#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    total = 0
    for t in my_list:
        sum += t[0] * t[1]
        total += t[1]
    return sum / total
