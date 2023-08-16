#!/usr/bin/python3
def uniq_add(my_list=[]):
    _set = set(my_list)
    answer = 0
    for i in _set:
        answer += i
    return (answer)
