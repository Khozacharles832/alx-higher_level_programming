#!/usr/bin/python3
"""Overriding method"""


class MyInt(int):
    '''derived class'''
    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
