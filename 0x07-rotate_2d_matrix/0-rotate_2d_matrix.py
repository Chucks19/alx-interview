#!/usr/bin/python3
"""_summary_ of how to rotate a matrix
"""


def transp_matrx(matrix, n):
    """SUMMARY: rotate a matrix

    Arguments:
                    matrix (type):description
    """
    for A in range(n):
        for B in range(i, n):
            matrix[A][B], matrix[B][A] = matrix[B][A], matrix[A][B]


def revers_matrx(matrix):
    """SUMMARY: reverse a matrix

    Arguments:
                    matrix (type):description
    """
    for rows in matrix:
        rows.reverse()


def rotate_2d_matrix(matrix):
    """_summary_

    Args:
                    matrix (_type_): _description_
    """
    na = len(matrix)
    # print(na)

    """sample matrix
    1 2 3
    4 5 6
    7 8 9
    """

    # transpose matrix
    """
    1 4 7
    2 5 8
    3 6 9
    """

    transp_matrx(matrix, na)

    # reverse matrix
    """
    7 4 1
    8 5 2
    9 6 3
    """
    revers_matrx(matrix)

    return matrix
