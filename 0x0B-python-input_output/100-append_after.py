#!/usr/bin/python3
"""Module with a function"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to a file"""
    text = ""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
