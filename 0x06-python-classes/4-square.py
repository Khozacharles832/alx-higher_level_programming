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

    @property
    def size(self):
        """ Returns the size of a square
        """

    @size.setter
    def size(self, value):
        """ Property setter for size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
