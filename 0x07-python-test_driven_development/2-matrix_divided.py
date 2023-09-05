#!/usr/bin/python3
"""
A module composed by a function that divides the numbers of a matrix
"""

def matrx_divided(matrix, div):
    """
        function that divides the int of a matrix
        matrix: list of a lists of int
        div: number which divides the matrix

        Return: Anew matrix with the result of the divivsion
        raise
        TypeError:
        ZeroDivionError
    """
    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in (int, float):
        raise TypeError ("div must be a number")
    if div == 0:
        raise ZeroDivisionError ("division by zero")
    
    len_row = set(len(row) for row in matrix)
    if len(len_row) != 1:
        raise TypeError ("Each row of the matrix must have the same size")

    new_matrix = [[round(item / div, 2) for item in row] for row in matrix]

    return (new_matrix)
