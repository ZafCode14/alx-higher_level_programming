#!/usr/bin/python3
"""Module with a function"""


def inherits_from(obj, a_class):
    """Function that returns True or False"""
    return type(obj) != a_class and isinstance(obj, a_class)
