#!/bin/python3

import sys


def insertionSort1(n, arr):
    # Complete this function
    val = arr[n]
    for i in range(n, 0, -1):
        arr[i] = arr[i - 1]
        if arr[i - 1] < val:
            arr[i] = val
            print(*arr)
            return
        else:
            print(*arr)
    arr[0] = val
    print(*arr)


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort1(n - 1, arr)

