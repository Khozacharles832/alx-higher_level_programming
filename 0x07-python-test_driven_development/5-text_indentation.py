#!/usr/bin/python3
"""A text indentation function"""


def text_indentation(text):
    """Indents text strings"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    inside_space = False

    for char in text:
        if char in (".", "?", ":"):
            result += char + "\n\n"
            inside_space = True
        elif char == " " and inside_space:
            inside_space = False
        result += char
    print(result)
