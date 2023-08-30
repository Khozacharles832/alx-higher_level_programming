#!/usr/bin/python3
"""" Defines a class square"""


class Square:
    """
    class that defines properties of a square by: (based on 2-square.py)

    Attributes:
        size: size of square ( side).
    """
    def __init__(self, size=0):
        """
        create a new instance of square

        Args:
            size: the size of square (1 side).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ calculates the length of the square

        Returns: the current square area
        """
        return (self.__size ** 2)
