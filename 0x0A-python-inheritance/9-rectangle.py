#!/usr/bin/python3
'''Module'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''derived class'''

    def __init__(self, width, height):
        '''Attr'''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''Method'''
        return self.__width * self.__height

    def __str__(self):
        '''To str'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
