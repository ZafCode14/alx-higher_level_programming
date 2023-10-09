#!/usr/bin/python3
"""Module with a class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Class with methods"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
