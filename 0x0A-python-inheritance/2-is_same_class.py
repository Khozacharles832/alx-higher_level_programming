#!/usr/bin/python3
"""
    module with the is_same_class method
"""


def is_same_class(obj, a_class):
    """Method that returns true if object is instance of class
    """
    return type(obj) is a_class
