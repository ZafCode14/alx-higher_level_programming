#!/usr/bin/python3
"""Module with a function"""


def say_my_name(first_name, last_name=""):
    """Function that print a string of the name

        Args:
            first_name (str): the first name
            Last_name (str): the last name

        Returns: nothing
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
