#!/usr/bin/python3
"""Module with a function"""


def class_to_json(obj):
    """Function that returns the dictionnary description"""
    return obj.__dict__
