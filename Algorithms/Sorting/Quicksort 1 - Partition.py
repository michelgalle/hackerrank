#!/bin/python3

import sys

def quickSort(arr):
    # Complete this function
    p = arr[0]
    left = []
    right = []
    for i in arr[1:]:
        if i < p:
            left.append(i)
        else:
            right.append(i)
    return( left + [p] + right )

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = quickSort(arr)
    print (" ".join(map(str, result)))


