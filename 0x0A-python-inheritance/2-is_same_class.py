#!/usr/bin/python3
""" Returns true if an object is exactly
an instance of the specified class """


def is_same_class(obj, a_class):
    """
    checks if an object is an exact isinstance of a class
    
    Args:
        obj: the object
        a_class: the class

    Returns:
        True or False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
