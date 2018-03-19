#!/bin/python3

import sys

'''mem = {}  # mem[(n,c)] = nb of ways to get n, using coins <=c
def make_change(coins, n):
    coins = sorted(coins, reverse=True)

    def dp(n, c):  # = nb of ways to get n, using coins <=c
        if n < 0: return 0
        if n == 0: return 1
        if (n, c) in mem: return mem[(n, c)]

        smaller_coins = filter(lambda coin: coin < c, coins)
        if len(smaller_coins) == 0: return 1 if n % c == 0 else 0
        next_coin = smaller_coins[0]

        ret = 0;
        remain = n
        while remain >= 0:
            ret += dp(remain, next_coin)
            remain -= c
        mem[(n, c)] = ret
        return ret

    return dp(n, coins[0])
'''


def make_change(coins, n):
    results = [1] + [0] * n
    for coin in coins:
        for i in range(coin, n + 1):
            results[i] += results[i - coin]
    return results[n]


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
coins = [int(coins_temp) for coins_temp in input().strip().split(' ')]
print(make_change(coins, n))
