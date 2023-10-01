#!/usr/bin/python3
"""Module with a funtion that adds two integers"""


def add_integer(a, b=98):
    """Function that adds 2 integers

    Args:
        a (int): first integer.
        b (int): secong integer.

    Returns:
        int: a plus b.
    """
    if not isinstance(a, (int ,float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int ,float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
