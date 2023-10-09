#!/usr/bin/python3
"""Module with a class"""


class MyInt(int):
    """Class with methods"""

    def __eq__(self, value):
        return self.real != value

    def __ne__(self, value):
        return self.real == value
