#!/usr/bin/python3
"""An empty class rectangle
"""


class Rectangle:
    """A class rectangle that creates private instance attributes

    Args:
        width (int): The width of the rectangle
        height (int): The height of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width getter property

        Returns:
            width (int): The width of the rectangle
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """The width setter property

        Args:
            value (int): The value to be set as the rectangles width

        Attributes:
            width (int): The width of the rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """The height property setter

        Returns:
            height (int): The height of the rectangle
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """The height property setter

        Args:
            value (int): The value to be set as the rectangles height

        Attributes:
            height (int): The height of the rectangle

        Raises:
            TypeError: height must be an int
            ValueError: height must be >= 0
        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise TypeError('height must be >= 0')
        self.__height = value
        
    def area(self):
        """Public instance method of the class Rectangle
            
        Returns:
            The area of the rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """Public instance method the rectangle class
        that returns the perimeter of the ractangle given the width and height

        Returns:
            0 if width or height is 0, else the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """prints instances of str

        Returns:
            The string representation of rectangle suitable for printing
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        else:
            rectangle_str = ""
            for _ in range(self.__height):
                rectangle_str += "#" * self.__width + "\n"
            return (rectangle_str[:-1])

    def __repr__(self):
        """Defines formal representation of object

        Returns:
            The string
        """
        return f"Rectangle({self.__width}, {self.__height})"



