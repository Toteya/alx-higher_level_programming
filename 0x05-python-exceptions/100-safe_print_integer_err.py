#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        err_message = f"Exception: {str(err)}\n"
        sys.stderr.write(str(err_message))
        return False
