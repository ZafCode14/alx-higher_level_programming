#!/usr/bin/python3
"""Module with a function"""


def add_attribute(obj, att, value):
    """Function with that adds new attr"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
