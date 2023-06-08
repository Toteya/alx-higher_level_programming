#!/usr/bin/python3
import sys


def main():
    num_args = len(sys.argv) - 1
    s = ""
    if num_args > 1:
        s = "s:"
    elif num_args == 1:
        s = ":"
    else:
        s = "s."
    print("{} argument{}".format(num_args, s))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
