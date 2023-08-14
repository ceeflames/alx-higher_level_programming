#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        matrix = []

    for row in matrix:
        current_row = row
        if not current_row:
            print()
        for element in current_rom:
            print("{:d}".format(element), end=" " if element != current_row[-1] else '\n')
