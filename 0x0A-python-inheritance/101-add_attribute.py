#!/usr/bin/python3
'''Add atribute function'''


def add_attribute(obj, attr, data):
    '''A function to add a new attibute'''
    if not hasattr(obj, '__dict__'):
        raise TypeError("Can't add new attribute")
