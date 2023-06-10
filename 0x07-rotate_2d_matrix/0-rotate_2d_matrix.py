<<<<<<< HEAD
#!/usr/bin/python3
"""Summary of Matrix rotation
"""


def transpose_matx(matrix, n):
    """_summary_

    Args:
       description_
    """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matx(matrix):
    """_summary_

    Args:
               description_
    """
    for row in matrix:
        row.reverse()


def rotate_2d_matx(matrix):
    """_summary_

    Args:
               _description_
    """
    n = len(matrix)
    # print(n)

    """sample matrix
    1 2 3
    """

    # traSpose matrix
    """
    1 4 7
    3 6 9
    """

    transpose_matx(matrix, n)

    # reverse matrix
    """
    7 4 1
    """
    reverse_matx(matrix)

    return matrix
=======
#!/usr/bin/python3
"""Summary of Matrix rotation
"""


def transpose_matx(matrix, n):
    """_summary_

    Args:
       description_
    """
    for A in range(n):
        for j in range(A, n):
            matrix[A][j], matrix[j][A] = matrix[j][A], matrix[A][j]


def reverse_matx(matrix):
    """_summary_

    Args:
               description_
    """
    for row in matrix:
        row.reverse()


def rotate_2d_matx(matrix):
    """_summary_

    Args:
               _description_
    """
    n = len(matrix)
    # print(n)

    """sample matrix
    1 2 3
    """

    # traSpose matrix
    """
    1 4 7
    3 6 9
    """

    transpose_matx(matrix, n)

    # reverse matrix
    """
    7 4 1
    """
    reverse_matx(matrix)

    return matrix
>>>>>>> f987a204b2d3fb91e0bcbf96058ef0ef38d2f336
