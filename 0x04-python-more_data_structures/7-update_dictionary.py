#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for up in a_dictionary:
            if up == key:
                a_dictionary[up] = value
    return (a_dictionary)
