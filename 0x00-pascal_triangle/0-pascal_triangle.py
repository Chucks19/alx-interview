#!/user/bin/python3

""" A script that determine pascal traingle for any number"""


def pascal_triangle(n):

    """ A function that returns a list of lists of numbers"""
    if n <= 0:
        return []
    pascal_tria = []
    for i in range(n):
        for j in range(i+1):
            temp_ar = []
            if i == 0:
                temp_ar.append(1)
            if i == 1:
                temp_ar.append(1)
            else:
                temp_ar.append([pascal_tria[i-1][j-1] + pascal_tria[i-1][j]])
        pascal_tria.append(temp_ar)
    return pascal_tria
