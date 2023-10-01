#!/usr/bin/python3
"""Defines write_file module"""


def write_file(filename="", text=""):
    """writes a new file"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            num_chars = file.write(text)
        return (num_chars)
    except Exception as e:
        print(f"Error writting to file: {e}")
        return (0)
