#!/usr/bin/python3
"""
Question: minimum number of coins to
achieve a given amount total
"""


def makeChange(coins, total):
    """ fewest number of coins needed to meet total """
    if total <= 0:
        return 0
    # sort the coins in descending order
    coins.sort(reverse=True)
    chnge = 0
    for coin in coins:
        if total <= 0:
            break
        tmp = total // coin
        chnge += tmp
        total -= (tmp * coin)
    if total != 0:
        return -1
    return chnge
