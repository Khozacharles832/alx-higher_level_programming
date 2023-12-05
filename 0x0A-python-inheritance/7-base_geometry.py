#!/usr/bin/python3
""" The BaseGeometry class """


class BaseGeometry():
    """The BaseGeometry class"""

    def area(self):
        """ The area public method

        Raises:
            Exception("area() is not implemented")
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ The integer_validator public method

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
