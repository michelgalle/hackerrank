#!/bin/python3

import sys
from collections import defaultdict

if __name__ == "__main__":
    pos = {}
    n = int(input().strip())
    for a0 in range(n):
        x, s = input().strip().split(' ')
        x, s = [int(x), str(s)]
        s = s if a0 >= n/2 else '-'
        if x in pos:
            pos[x].append(s)
        else:
            pos[x] = [s]
    for k, v in pos.items():
        print(' '.join(v),end=' ')
