#!/usr/bin/python3
"""Defines the append file module"""



def append_write(filename="", text=""):
    """Appends text at the end of a file"""
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            num_chars = file.write(text)
        return (num_chars)
    except Exception as e:
        print(f"Error appending to file: {e}")
        return (0)
