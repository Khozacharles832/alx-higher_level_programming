#!/usr/bin/python3
"""Defines the inherits from method"""


def inherits_from(obj, a_class):
    """Returns True if obj inherited or is an
    instance of the class
    """

    return False if type(obj) is a_class else isinstance(obj, a_class)
