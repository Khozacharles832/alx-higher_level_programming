#!/usr/bin/python3
"""divides a list of lists"""


def matrix_divided(matrix, div):
    """Divides all the elements of a matrix by a divisor

    Args:
        matrix(list): A list of lists containing integers/ floats
        dev  (int/float): the divisor to divide each element in the matrix

    Raises:
        TypeError: if matrix is not a list of lists of integers / floats
                   if the matrix contains rows of different sizes
                   if div is not an int / float
        ZeroDivisionError: if div is 0

    Returns:
        list: a new matrix representing the result of the division
    """
    #check if the input matrix is correct
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                "integers/floats")

    #check if all rows of the list have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    #check if div is a valid number
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    #check for division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    #perfom matrix division and rounding
    result = [
            [round(num / div, 2) for num in row]
            ]
    return (result)
