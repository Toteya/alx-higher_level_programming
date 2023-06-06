#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if ld > 5:
    a = "greater than 5"
elif ld == 0:
    a = "0"
else:
    a = "less than 6 and not 0"
print(f"The last digit of {number:d} is {ld} and is {a}")
