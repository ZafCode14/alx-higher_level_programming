#!/usr/bin/python3
"""Module with a function"""

def inherits_from(obj, a_class):
    """Function that returns True or False"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
