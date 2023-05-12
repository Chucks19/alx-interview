#!/usr/bin/python3
'''mini Operation challenge'''

def minOperations(n):
    '''calculates the minimum number of
    operations for exactly n H
    characters in this file.
    Returns:
        Integer : if n is impossible, return 0
    '''
    if not isinstance(n, int)
    pasted_ch = 1  # amount chars in the fil
    cliboard = 0  # amount H's copied
    couter = 0  # operations counter

    while pasted_ch < n:
        # if did not copy anything yet then
        if cliboard == 0:
            # copyall
            cliboard = pasted_ch
            # increment counter
            couter += 1
        # if haven't pasted anything yet
        if pasted_ch == 1:
            pasted_ch += cliboard
            # increment operations counter
            couter += 1
            # continue to next loop
            continue
        remaini = n - pasted_ch  # remaining chars to Paste check if impossible by checking if clipboard
        # has more than needed to reach the number desired which also means num of chars in file is equal
        # or more than in the clipboard. in both situations it's impossible to achieve n of chars
        if remaini < cliboard:
            return 0

        # if can't be devided
        if remaini % pasted_ch != 0:
            # paste current clipboard
            pasted_ch += cliboard
            # increment operations counter
            couter += 1
        else:
            # copyall
            cliboard = pasted_ch
            # paste
            pasted_ch += cliboard
            # increment operations counter
            couter += 2

    # if got the desired result
    if pasted_ch == n:
        return couter
    else:
        return 0
    