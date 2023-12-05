#!/usr/bin/python3
"""Returns a list of attributes an methods"""


def lookup(obj):
    """Returns all attributes and methods
    Args:
        obj: the object

    Returns:
        list
    """
    return dir(obj)
