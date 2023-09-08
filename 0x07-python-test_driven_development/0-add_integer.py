#!/usr/bin/python3
"""defines an integer addition function"""


def add_integer(a, b=98):
    """Returns the addition of 2 numbers

    floats arguments are typecasted to int before addition

    Raises:
        TypeError: if either a or b is non int or non float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
