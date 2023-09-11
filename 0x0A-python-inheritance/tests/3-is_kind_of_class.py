#!/usr/bin/python3
"""
Defines the is kind 0f class method
"""


def is_kind_of_class(obj, a_class):
    """Returns true if obj inherited or is an instance
    of the class
    """

    return isinstance(obj, a_class)
