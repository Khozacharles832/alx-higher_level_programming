#!/usr/bin/python3
def search_replace(my_list, search, replace):
    _list = []
    for i in my_list:
        if i != search:
            _list.append(i)
        else:
            _list.append(replace)
    return (_list)
