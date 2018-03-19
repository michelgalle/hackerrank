#!/bin/python3

import sys

g = int(input().strip())
for a0 in range(g):
    n, m, x = input().strip().split(' ')
    n, m, x = [int(n), int(m), int(x)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))

    a.reverse()
    b.reverse()

    c = []
    m_num = 0
    s1 = 0

    while a != []:
        if s1 + a[-1] <= x:
            c.append(a.pop())
            s1 += c[-1]
            m_num += 1
        else:
            break

    s2 = 0

    while b != []:
        if s2 + b[-1] <= x:
            if s1 + b[-1] <= x:
                el = b.pop()
                s1 += el
                s2 += el
                m_num += 1
            else:
                el = b.pop()
                s1 += el - c.pop()
                s2 += el
        else:
            break

    print(m_num)