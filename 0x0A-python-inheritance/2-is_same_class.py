#!/usr/bin/python3
"""Module with a function"""


def is_same_class(obj, a_class):
    """Function that check the class"""
    if type(obj) == a_class:
        return True
    else:
        return False
