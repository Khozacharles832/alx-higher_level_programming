#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, data):
        if not isinstance(data, int):
            raise TypeError("size must be an integer")
        elif data < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = data
