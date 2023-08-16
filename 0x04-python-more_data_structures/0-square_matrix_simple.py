#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for values in matrix:
        new_matrix.append([i ** 2 for i in values])
    return (new_matrix)
