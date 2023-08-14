#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    _len = len(my_list) - 1
    if (idx < 0 or idx > _len):
        return (my_list)
    else:
        _list = my_list[:]
        _list[idx] = element
        return (_list)
