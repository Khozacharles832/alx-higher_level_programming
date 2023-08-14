#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    _len = len(my_list) - 1
    if (idx < 0 or idx > _len):
        return (my_list)
    else:
        my_list[idx] = element
        return (my_list)
