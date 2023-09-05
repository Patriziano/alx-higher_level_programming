#!/usr/bin/python3
""" a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix (list of lists of int or float): The input matrix.
        div (int or float): The divisor.
    Raises:
        TypeError: if matrix is not a list of int/float
                    if matrix is not of the same size
                    if div is not an int/float
        ZeroDivisonError: if div is zero

    Returns:
        list of lists of float: A new matrix with elements divided by 'div'
            rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix == [] or not (isinstance(matrix, list)):
        raise TypeError(msg)
    if not all(isinstance(row, list) and
               all(isinstance(value, (int, float)) for value in row)
               for row in matrix):
        raise TypeError(msg)

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(value / div, 2) for value in row] for row in matrix]

    return new_matrix
