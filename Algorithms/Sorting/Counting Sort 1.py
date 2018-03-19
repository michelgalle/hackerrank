#!/bin/python3

import sys

def countingSort(arr):
    # Complete this function
    nbr = [0]*100
    for i in arr:
        nbr[i] += 1
    return nbr

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = countingSort(arr)
    print (" ".join(map(str, result)))


