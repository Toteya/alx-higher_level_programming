#!/usr/bin/python3
num1, op, num2 = input("Enter calculation: ").split()

num1 = int(num1)
num2 = int(num2)

if op == '+':
    sum = num1 + num2
    print("{} + {} = {}".format(num1, num2, sum))
