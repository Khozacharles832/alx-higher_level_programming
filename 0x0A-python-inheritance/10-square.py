#!/usr/bin/python3
""" The Rectangles child class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ The square class """
    def __init__(self, size):
        self.__size = size
        BaseGeometry.integer_validator(self, "size", size)
        super().__init__(size, size)

    def area(self):
        """ the size method """
        return self.__size ** 2
