#!/usr/bin/python3
"""
Question: minimum number of coins to
achieve a given amount total
"""


def makChnge(coins, total):
    """ fewest number of coins needed to meet total """
    if total <= 0:
        return 0
    # sort the coins in descending order
    coins.sort(reverse=True)
    chnge = 0
    for coin in coins:
        if total <= 0:
            break
        temp = total // coin
        chnge += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return chnge
