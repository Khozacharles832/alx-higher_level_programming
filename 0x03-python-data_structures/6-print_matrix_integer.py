#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        _len = 1
        for elem in row:
            if _len == len(row):
                print("{:d}".format(elem), end="")
            else:
                print("{:d}".format(elem), end=" ")
            _len += 1
        print()
