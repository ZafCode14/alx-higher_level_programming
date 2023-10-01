#!/usr/bin/python3
"""Module with a function"""


def print_square(size):
    """Function that prints a square
    Args:
        size (int): the length of the square
    Returns:
        nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size, end="")
        print()
