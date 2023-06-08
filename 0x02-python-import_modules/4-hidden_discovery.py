#!/usr/bin/python3
import hidden_4


def main():
    names = sorted(dir(hidden_4))
    for name in names:
        if name[0] != "_":
            print("{}".format(name))


if __name__ == "__main__":
    main()
