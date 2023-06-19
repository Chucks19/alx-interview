#!/usr/bin/python3
"""Island Perimeter - ALX Interview"""


def check_value(x):
    """_summary_

    Args:
    description_

    Returns:
    _description_
    """
    if (x == 0):
        return 1
    return 0


def island_perimeter(grid):
    """_summary_

    Args:
        grid (_type_): _description_
    """

    rows = len(grid)
    cols = len(grid[0])
    assert (1 <= rows and cols <= 100), "len must be between 1 an 100"

    x = 0
    for ia in range(rows):
        for ja in range(cols):
            assert (grid[ia][ja] == 0) or (grid[ia][ja] == 1),\
                "grid numbers must be 0 or 1"
            if grid[ia][ja] == 1:
                if ia-1 < 0:
                    x += 1
                else:
                    x += check_value(grid[ia-1][ja])
                if ja-1 < 0:
                    x += 1
                else:
                    x += check_value(grid[ia][ja-1])

                try:
                    x += check_value(grid[ia+1][ja])
                except IndexError:
                    x += 1
                try:
                    x += check_value(grid[ia][ja+1])
                except IndexError:
                    x += 1

    return x
