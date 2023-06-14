#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    def square(num):
        return num ** 2
    new_mat = list(map(lambda row: list(map(square, row)), matrix))
    return new_mat
