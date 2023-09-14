#!/usr/bin/python3
"""defines a class student"""


class student:
    """the student class"""
    def __init__(self, first_name, last_name, age):
        """the method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representantion of student instance
        Args:
            attrs: a list of attribute names

        Returns:
            dict: a dictionary represantation
        """
        if attrs is None:
            return {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'age': self.age
                    }
        else:
            new_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    new_dict[attr] = getattr(self, attr)
            return (new_dict)

