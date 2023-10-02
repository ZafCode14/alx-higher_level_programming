#!/usr/bin/python3
"""Module with a class"""


class Rectangle:
    """Class that represents a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializing rectangle
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method that returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Mothod that returns the perimeter"""
        if self.__width == 0 or self.__height == 0:
            result = 0
        else:
            result = (2 * self.__width) + (2 * self.__height)
        return result

    def __str__(self):
        """prints the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        for i in range(self.__height):
            rectangle += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """prints the representation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
