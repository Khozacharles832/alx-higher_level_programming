#!/usr/bin/python3
"""
Defines with class BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry class"""

    
    def area(self):
        """calculate area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if num is an int or not"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
