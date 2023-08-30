#!/usr/bin/python3
""" Defines a class square """


class Square:
    """ class that defines the properties of a square by: (5-square.py)
        
        Attributes:
            size: size of the square (1 side).
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """ calculates the area of the square

            Returns:
                the area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
            Returns the size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, data):
        """
            property setter for size

            Args:
                value (int): size of a square (1 side).

            Raises:
                TypeError: size must be an integer
                ValueError: size must be >= 0
        """
        if not isinstance(data, int):
            raise TypeError("size must be an integer")
        if data < 0:
            raise ValueError("size must be >= 0")
        self.__size = data

    @property
    def position(self):
        """ Returns the position of the square
        """
        return (self.__position)

    @position.setter
    def position(self, data):
        """ property setter for position

        Args:
            value (tuple): position of the square

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(data, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(data) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(data[0], int) or not isinstance(data[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if data[0] < 0 or data[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = data

    def my_print(self):
        """
            prints the # char to stdout
        """
        if self.__size == 0:
            print()
        else:
            for j in range(self.__size):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)
