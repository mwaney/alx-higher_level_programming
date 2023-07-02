#!/usr/bin/python3
"""A module to divide the elements of a matrix
according to the divisor given
"""


def matrix_divided(matrix, div):
    """Divides each element of the matrix by the divisor.

    Args:
        matrix (list): A matrix (list of lists) containing integers or floats.
        div (int or float): The divisor.

    Raises:
        TypeError: If the matrix is not a matrix
        (list of lists) of integers/floats.
        TypeError: If the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.
        TypeError: If the rows of the matrix have different sizes.

    Returns:
        list: A new matrix (list of lists) with each
        element divided by the divisor and rounded to two decimal places.
    """
    output = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(output)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix2 = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError(output)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        list1 = []
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(output)
            list1.append(round(i / div, 2))
        matrix2.append(list1)
    return matrix2
