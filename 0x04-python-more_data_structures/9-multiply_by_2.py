#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    _new = a_dictionary.copy()
    for key, value in _new.items():
        _new[key] = value * 2
    return (_new)
