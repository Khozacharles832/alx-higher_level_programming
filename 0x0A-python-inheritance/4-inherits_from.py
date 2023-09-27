#!/usr/bin/python3
"""
module with the inherits from method
"""


def inherits_from(obj, a_class):
    """A method that returns true if object is instance of class"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
