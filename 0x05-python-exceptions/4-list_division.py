#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    _new = []
    for i in range(list_length):
        try:
            data_1 = my_list_1[i]
            data_2 = my_list_2[i]

            if not isinstance(data_1, (int, float)) or not isinstance(data_2, (int, float)):
                print("wrong type")
                res = 0
            elif data_2 == 0:
                print("division by 0")
                res = 0
            else:
                res = data_1 / data_2
        except IndexError:
            print("out of range")
            res = 0
        _new.append(res)
    return (_new)
