#!/usr/bin/python3
"""Module with a function"""


def write_file(filename="", text=""):
    """Function that writes to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
