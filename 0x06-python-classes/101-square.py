#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, data):
        if not isinstance(data, int):
            raise TypeError("size must be an integer")
        if data < 0:
            raise ValueError("size must be >= 0")
        self.__size = data

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, data):
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
        if self.__size == 0:
            print()
        else:
            for j in range(self.__size):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)

    def __str__(self):
        if self.__size == 0:
            return ('')
        positions = '\n' * self.position[1]
        character = ' ' * self.position[0]
        symbol = '#' * self.size
        return (positions + '\n'.join(character + symbol for i in range(self.size)))
