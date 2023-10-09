#!/usr/bin/python3
"""Module with a class"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        print(sorted(self));
