#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
ld = math.fmod(number, 10)
if ld > 5:
    a = "greater than 5"
elif ld == 0:
    a = "0"
    ld = 0
else:
    a = "less than 6 and not 0"
print(f"Last digit of {number:d} is {ld:.0f} and is {a}")
