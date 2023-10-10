#!/usr/bin/python3
"""Module with a function"""


def append_write(filename="", text=""):
    """Function that appends a sting at the end of a text file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
