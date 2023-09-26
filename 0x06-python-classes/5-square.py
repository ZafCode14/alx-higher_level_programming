#!/usr/bin/python3
"""Dine a class Square"""


class Square:
    """Initialise size"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    def area(self):
        return self.size * self.size

    def my_print(self):
        for i in range(self.size):
            print("#" * self.size)
        if self.size == 0:
            print()
