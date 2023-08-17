#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    res = a_dictionary.copy()
    _list = list(res.keys())
    for i in _list:
        res[i] *= 2
    return (res)
