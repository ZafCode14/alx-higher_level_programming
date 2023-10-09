#!/usr/bin/python3
"""Module with a function"""


def lookup(obj):
    """Function that returns the list of available attributes
        and methods of an object
    Args:
        obj - object
    """
    return dir(obj)
