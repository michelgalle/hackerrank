#!/bin/python3

import sys

def runningTime(a):
    nbr = 0
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            nbr += 1
            a[j+1]=a[j]
            j=j-1
        a[j+1]=key
    return nbr

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = runningTime(arr)
    print(result)
