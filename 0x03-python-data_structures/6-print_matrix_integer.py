#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None or len(matrix) == 0:
        return (None)

    for row in matrix:
        current_row = row
        if not current_row:
            print()
        for element in current_row:
            print("{:d}".format(element), end=" " if element != current_row[-1] else '\n')
