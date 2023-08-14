#!/usr/bin/python3
def no_c(my_string):
    _str = []
    for char in my_string:
        if char != 'c' and char != 'C':
            _str.append(char)
    return (''.join(_str))
