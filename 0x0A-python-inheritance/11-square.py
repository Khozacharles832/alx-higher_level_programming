#!/usr/bin/python3

Rectangle = __import__('9-rectangle').Rectangle
'''BaseGeometry module'''


class Square(Rectangle):
    '''Derived class'''

    def __init__(self, size):
        '''Initialize attributes'''
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''The rectangles area'''
        return self.__size * 2

    def __str__(self):
        return "[square] {}/{}".format(self.__size, self.__size)
