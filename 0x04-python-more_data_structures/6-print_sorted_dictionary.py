#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    _new = list(a_dictionary.keys())
    _new.sort()
    for i in _new:
        print("{} : {}".format(i, a_dictionary.get(i)))
