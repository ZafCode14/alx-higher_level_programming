#!/usr/bin/python3
"""Module with a function"""


def text_indentation(text):
    """Function that indents the text

    Args:
        text (str): the text to modify
    Return:
        nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    indented_text = ""
    skip_whitespace = True
    newline_chars = [".", "?", ":"]

    for char in text:
        if char in newline_chars:
            indented_text += char + "\n\n"
            skip_whitespace = True
        elif char == " " and skip_whitespace:
            continue
        else:
            indented_text += char
            skip_whitespace = False

    print(indented_text)
