#!/bin/python3

import sys

n1, n2, n3 = input().strip().split(' ')
n1, n2, n3 = [int(n1), int(n2), int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

if len(h1) == 0 or len(h2) == 0 or len(h3) == 0:
    print(0)

h1.reverse()
h2.reverse()
h3.reverse()
for i in range(1, len(h1)):
    h1[i] += h1[i - 1]
for i in range(1, len(h2)):
    h2[i] += h2[i - 1]
for i in range(1, len(h3)):
    h3[i] += h3[i - 1]

while True:
    lh1 = len(h1) - 1
    lh2 = len(h2) - 1
    lh3 = len(h3) - 1
    #print(h1, end='')
    #print(h2, end='')
    #print(h3)
    if lh1 < 0 or lh2 < 0 or lh3 < 0:
        print(0)
        break
    if h1[lh1] == h2[lh2] and h1[lh1] == h3[lh3]:
        print(h1[lh1])
        break
    if h1[lh1] > h2[lh2] or h1[lh1] > h3[lh3]:
        h1.pop()
        lh1 -= 1
        if lh1 < 0:
            print(0)
            break
    if h2[lh2] > h3[lh3] or h2[lh2] > h1[lh1]:
        h2.pop()
        lh2 -= 1
        if lh2 < 0:
            print(0)
            break
    if h3[lh3] > h2[lh2] or h3[lh3] > h1[lh1]:
        h3.pop()

