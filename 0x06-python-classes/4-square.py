#!/usr/bin/python3
"""Define a class Square"""
class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size (int): the size of the new square
        """
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
