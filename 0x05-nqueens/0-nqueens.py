#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""


import sys


def generate_sols(row, column):
    solut = [[]]
    for n in range(row):
        solut = place_qun(n, column, solut)
    return solut


def place_qun(n, column, prev_solut):
    safe_posit = []
    for arr in prev_solut:
        for x in range(column):
            if is_safe(n, x, arr):
                safe_posit.append(arr + [x])
    return safe_posit


def is_safe(q, x, arr):
    if x in arr:
        return (False)
    else:
        return all(abs(arr[column] - x) != q - column
                   for column in range(q))


def init():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return (n)


def n_queens():

    n = init()
    # generate all solutions
    solut = generate_sols(n, n)
    # print solutions
    for arr in solut:
        clean = []
        for q, x in enumerate(arr):
            clean.append([q, x])
        print(clean)


if __name__ == '__main__':
    n_queens()
