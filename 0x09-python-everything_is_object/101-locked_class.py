#!/usr/bin/python3
"""Module with a class"""


class LockedClass:
    """Class that prevents dynamically created new instance attributes"""
    __slots__ = ["first_name"]
