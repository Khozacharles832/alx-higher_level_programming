#!/usr/bin/python3
""" Defines a class square """


class Square:
    """
    class that defines the properties of a square by: (based on 1-square.py)

    Attributes:
        __size (int): size of the square (default is 0).
    """
    def __init__(self, size=0):
        """

            Initializes an instance of square class.

            Args:
                size: int size of square.
                must be an integer else raise TypeError exception.
                must be >= 0, else raise ValueError exception.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
