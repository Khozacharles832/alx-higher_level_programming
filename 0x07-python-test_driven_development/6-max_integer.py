#!/usr/bin/python3
'''The ``max_integers`` module'''


def max_integer(list=[]):
    '''max_integer module'''
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return (result)
