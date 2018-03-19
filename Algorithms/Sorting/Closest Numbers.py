#!/bin/python3

import sys


def closestNumbers(arr):
    arr.sort()
    lowestDiff = arr[1] - arr[0]
    res = [arr[0], arr[1]]
    for i in range(2, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff < lowestDiff:
            res = [arr[i-1]]
            res.append(arr[i])
            lowestDiff = diff
        elif diff == lowestDiff:
            res.append(arr[i-1])
            res.append(arr[i])
    return res

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = closestNumbers(arr)
    print (" ".join(map(str, result)))


