#!/usr/bin/python3
""" Returns a Boolean if obj is an instance od a_class"""


def inherits_from(obj, a_class):
    """ Return a Boolean based on inheritance
    Args:
        obj: object
        a_class: class

    Returns:
        True or False
    """
    return False if type(obj) is a_class else isinstance(obj, a_class)
