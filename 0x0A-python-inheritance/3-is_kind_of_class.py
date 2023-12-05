#!/usr/bin/python3
""" Returns a Boolean based on whether it is an instance or not """


def is_kind_of_class(obj, a_class):
    """ Return a Boolean on obj

    Args:
        obj: object
        a_class: class

    Returns:
        True or False
    """
    if isinstance(obj, a_class) is True:
        return True
    else:
        return False
