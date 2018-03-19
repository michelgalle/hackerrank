#!/bin/python3

import sys


def lonely_integer(a):
    n = 0
    for i in a:
        #xor negando os numeros, assim sobra somente o numero unico
        n ^= i
    return n


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
