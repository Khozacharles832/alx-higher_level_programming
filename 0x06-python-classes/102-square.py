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

    def __less_than_(self, value):
        return (self.__size < value.__size)

    def __less_eq__(self, value):
        return (self.__size <= value.__size)

    def __equaly__(self, value):
        return (self.__size == value.__size)

    def __not_eq__(self, value):
        return (self.__size != value.__size)

    def __grt__(self, value):
        return (self.__size > value.__size)

    def __grt_eq__(self, value):
        return (self.__size >= value.__size)
