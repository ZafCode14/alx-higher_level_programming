#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) and len(value) != 2 and not all(isinstance(element, int) for element in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.size * self.size

    def my_print(self):
        for k in range(self.position[1]):
            print()
        for i in range(self.size):
            for j in range(self.position[0]):
                print(" ", end="")
            print("#" * self.size)
        if self.size == 0:
            print()
