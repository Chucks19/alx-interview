#!/usr/bin/python3
""" Solution to Prime Game Programming"""

def isWinner(x, nums):
    """This function checks for the winner"""
    if not nums or x < 1:
        return None
    maximum_Num = max(nums)

    my_Filters = [True for _ in range(max(maximum_Num + 1, 2))]
    for i in range(2, int(pow(maximum_Num, 0.5)) + 1):
        if not my_Filters[i]:
            continue
        for j in range(i * i, maximum_Num + 1, i):
            my_Filters[j] = False
    my_Filters[0] = my_Filters[1] = False
    y = 0
    for i in range(len(my_Filters)):
        if my_Filters[i]:
            y += 1
        my_Filters[i] = y
    player1 = 0
    for x in nums:
        player1 += my_Filters[x] % 2 == 1
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 > len(nums):
        return "Maria"
    return "Ben"
