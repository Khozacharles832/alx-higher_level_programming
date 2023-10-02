#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
'''BaseGeometry class'''


class Square(Rectangle):
    '''Derived class'''

    def __init__(self, size):
        '''Attribute initializer'''
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def are(self):
        '''rectangle area'''
        return self.__size ** 2
