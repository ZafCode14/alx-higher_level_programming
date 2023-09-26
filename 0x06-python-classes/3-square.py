#!/usr/bin/python3
"""Define a class Square."""
class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): the size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be and integer")
        else:
            if (size < 0):
                raise ValueError("size must be >= 0")
            self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size