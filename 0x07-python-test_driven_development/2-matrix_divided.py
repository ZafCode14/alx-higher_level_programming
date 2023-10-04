#!/usr/bin/python3
"""Module with a function"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix

    Args:
        matrix (int, float): matrix of integers.
        div (int, float): a number to divide the matrix.

    Returns:
        a new matrix
    """

    if not isinstance(matrix, list):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if not all(all(isinstance(v, (int, float)) for v in r)for r in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    new_matrix = [[round((val / div), 2) for val in row] for row in matrix]

    return new_matrix
