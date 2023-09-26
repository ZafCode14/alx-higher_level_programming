#!/usr/bin/python3
"""Define a class Square."""
class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): the size of the new square
        """
        if isinstance(size, int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be and interger")