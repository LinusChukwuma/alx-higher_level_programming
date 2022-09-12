#!/usr/bin/python3
<<<<<<< HEAD
# 101-safe_function.py
=======
# 100-safe_print_integer_err.py
>>>>>>> 637c5c3254bcf28eeb705bb4a6af4b1f8b08fc32
# Brennan D Baraban <375@holbertonschool.com>

import sys


<<<<<<< HEAD
def safe_function(fct, *args):
    """Executes a function safely.

    Args:
    fct: The function to execute.
    args: Arguments for fct.

    Returns:
    If an error occurs - None.
    Otherwise - the result of the call to fct.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
=======
def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
>>>>>>> 637c5c3254bcf28eeb705bb4a6af4b1f8b08fc32
