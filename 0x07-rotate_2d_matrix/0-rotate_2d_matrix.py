#!/usr/bin/python3
'''
Rotates 2D Matrix
'''


def rotate_2d_matrix(matrix):
    '''
    Rotates a 2d Matrix
    '''
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
