#!/usr/bin/python3
""" Appends text to the end of file """


def append_write(filename="", text=""):
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
