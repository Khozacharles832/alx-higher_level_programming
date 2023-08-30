#!/usr/bin/python3
"""Defines a class square """


class Square:
    """
    defines properties of a square based on (3-square.py).

    Attributes:
        size: size of a square (1 side)
    """
    def __init__(self, size=0):
        """creates an instance of a square

        Args:
            size: the size of a square
        """
        self.__size = size

    def area(self):
        """calculates the area of a square

        Returns: the area of a square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """calculates the size of the square

        Returns: the size of the square (1 side).
        """
        return (self.__size)

    @size.setter
    def size(self, data):
        """setter for the size

        Args:
            data: the data

            Raises: TypeError: size must be an integer
                    ValueError: size must be >= 0
        """
        if not isinstance(data, int):
            raise TypeError("size must be an integer")
        elif data < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = data

    def __lt__(self, other):
        """less than operataor

        Returns: True / False
        """
        return (self.__size < other.__size)

    def __le__(self, other):
        """less than or equal to operator

        Returns: True / False
        """
        return (self.__size <= other.__size)

    def __eq__(self, other):
        """equality operator

        Returns: True / False
        """
        return (self.__size == other.__size)

    def __ne__(self, other):
        """Greater than and equal to

        Returns: True / False
        """
        return (self.__size != other.__size)

    def __gt__(self, other):
        """Greater than operator

        Returns: True / False
        """
        return (self.__size > other.__size)

    def __ge__(self, other):
        """Greater than and equal to

        Returns: True / False
        """
        return (self.__size >= other.__size)
