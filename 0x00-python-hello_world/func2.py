#!/usr/bin/python3
def calc(a, b):
    return 98 + (a ** b)

from dis import dis as c
c(calc)
