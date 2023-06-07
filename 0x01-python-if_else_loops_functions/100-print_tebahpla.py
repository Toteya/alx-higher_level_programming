#!/usr/bin/python3
for i in reversed(range(26)):
    if i % 2 == 0:
        i += ord('A')
    else:
        i += ord('a')
    print(chr(i), end="")
