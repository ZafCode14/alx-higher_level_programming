#!/usr/bin/python3
"""Module with a function"""


def is_same_class(obj, a_class):
    """Function that check the class"""
    if (isinstance(obj, a_class) == 0):
        return True
    else:
        return False
