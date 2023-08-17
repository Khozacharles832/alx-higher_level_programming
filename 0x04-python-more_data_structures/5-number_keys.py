#!/usr/bin/pyhon3
def number_keys(a_dictionary):
    res = 0
    _keys = list(a_dictionary.keys())
    for i in _keys:
        res += 1
    return (res)
