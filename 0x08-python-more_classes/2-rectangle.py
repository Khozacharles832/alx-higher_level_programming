#!/usr/bin/python3
'''A continution of the reectangle module'''


class Rectangle:
    '''Rectangle class

    Args:
        width (int): The horizontal size of the rectangle
        height (int): The vertical size of the rectangle
    '''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''The width getter

        Returns:
            width (int): The horizontal size of the rectangle
        '''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''The width setter

        Args:
            value (int): The int value assigned to width

        Attributes:
            width (int): The horizontal part of the rectangle

        Raises:
            TypeError: If value is not an int
            ValueError: If value is < 0
        '''
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''The height getter

        Returns:
            height (int): The vertical part of the rectangle
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''The height setter

        Args:
            value (int): The vertical size of the rectangle

        attributes:
            height (int): The rectangles height

        Raises:
            TypeError: If height is not an int
            ValueError: If height is less than zero
        '''
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__hieght = value

    def area(self):
        '''Returns the area of the rectangle width * height

        Attributes:
            width (int): The horizontal size of the rectsngle
            height (int): The vertical size of the rectangle

        Returns:
            area: width * height
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        '''The rectangles perimeter method

        Attributes:
            width (int): the rectangles width
            height (int): the rectangles height
        Returns:
            0 if either attr is 0 / the rectangles perimeter
        '''
        return (self.__width * 2) + (self.__height * 2)
