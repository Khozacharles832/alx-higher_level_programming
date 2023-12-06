#!/usr/bin/python3
""" Appends text to the end of file """


def append_write(filename="", text=""):
    """Appends text to end of file."""
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
