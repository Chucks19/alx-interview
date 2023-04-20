#!/usr/bin/python3
"""A script to determine pascal's triangle for any number"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triagle = []

    # return (trianlgle if n <= 0)
    if n <= 0:
        return triagle
    for i in range(n):
        temp_lit = []

        for j in range(i+1):
            if j == 0 or j == i:
                temp_lit.append(1)
            else:
                temp_lit.append(triagle[i-1][j-1] + triagle[i-1][j])
        triagle.append(temp_lit)
    # print(triagle)
    return triagle
