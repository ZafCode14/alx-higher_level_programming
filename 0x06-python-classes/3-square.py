#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Initialize size"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be and integer")
        else:
            if (size < 0):
                raise ValueError("size must be >= 0")
            self.__size = size

    def area(self):
        return self.__size * self.__size
