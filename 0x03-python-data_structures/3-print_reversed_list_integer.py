#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    _list = my_list[:: - 1]
    for i in _list:
        print("{:d}".format(i))
