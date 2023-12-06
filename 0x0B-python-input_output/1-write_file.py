#!/usr/bin/python3
""" Write or create a file and return it's length """


def write_file(filename="", text=""):
    """Writes to stdout and returns the length"""
    with open(filename, 'w', encoding='UTF-8') as f:
        return f.write(text)
