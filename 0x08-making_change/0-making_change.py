#!/usr/bin/python3
'''
Making change
'''


def makeChange(coins, total):
    '''
    Determines the fewest number of coins needed to
    meet a given amount total
    '''
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        count += total // coin
        total %= coin

    return count if total == 0 else -1
