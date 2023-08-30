#!/usr/bin/python3
"""Define a class magic class"""


class MagicClass:
    """
    class that defines properties of magic class

    Attributes:
        radius: radius
    """
    def __init__(self, radius=0):
        """Defines a new instance of magic class

        Args:
            radius: radius
        Raises:
            TypeError: radius must be a number
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

        def area(self):
            """returns area"""
            return (math.pi * self.__radius ** 2)

        def circumference(self):
            """Uses the circumfrance"""
            return (2 * math.pi * self.__radius)
