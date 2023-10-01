#!/usr/bin/python3
"""Defines module file read"""


def read_file(filename=""):
    """Read a file"""
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end="")
