#!/usr/bin/python3
"""Module with a function"""


def read_file(filename=""):
    """Function that reads file"""
    my_file = open(filename, 'r', encoding="utf-8")
    read_data = my_file.read()
    print(read_data, end="")
    my_file.close()
