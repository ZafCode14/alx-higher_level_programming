#!/usr/bin/python3
"""Module with a function"""
import json


def to_json_string(my_obj):
    """Function that returns the JSON representation of an object"""
    return json.dumps(my_obj)
