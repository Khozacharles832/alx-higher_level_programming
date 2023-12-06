#!/usr/bin/python3
""" The student class """


class Student:
    """ The student class """

    def __int__(self, first_name, last_name, age):
        """The attrs init method."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """The to json method."""
        if attrs is None:
            return self.__dict__
        new_dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dictionary[key] = value
            return new_dictionary
