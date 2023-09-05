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

