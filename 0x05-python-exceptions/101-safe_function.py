#!/bin/usr/python3
import sys


def safe_function(fct, *args):
    try:
        fct(*args)
    except Exception as e:
        print("Error: {}".format(e), file=sys.stderr)
        return None
