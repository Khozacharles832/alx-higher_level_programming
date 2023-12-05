#!/usr/bin/python3
""" A Rectangle class inheriting from the BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ The base geometry child class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ The area method """
        return (self.__width * self.__height)

    def __str__(self):
        """ returns the string represantation of obj """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
