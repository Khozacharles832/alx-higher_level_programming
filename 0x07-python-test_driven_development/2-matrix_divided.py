#!/usr/bin/python3

def matrix_divided(matrix, div):
    '''Divides a matrix by div an int'''
    new_matrix = []
    new_list = []
    if not matrix:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be number')
    if div is 0:
        raise ZeroDivisionError('division by zero')
    list_size = len(matrix[0])
    for part in matrix:
        if type(part) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(part) != list_size:
            raise TypeError('Each row of the matrix must have the same size')
        for item in part:
            if type(item) is not int and type(item) is not float:
                raise TypeError('matrix must be a matrix (list if lists) of integers/floats')
            num = item / div
            new_list.append(round(num, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix

