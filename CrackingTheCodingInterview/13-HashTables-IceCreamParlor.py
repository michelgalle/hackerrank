#!/bin/python3

import sys


def binarysearch(sequence, lo, value):
    hi = len(sequence) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if sequence[mid] < value:
            lo = mid + 1
        elif value < sequence[mid]:
            hi = mid - 1
        else:
            return mid
    return None


def index_of(arr, value, exclude_this):
    for i, val in enumerate(arr):
        if val == value and i != exclude_this:
            return i
    return None


def get_idx_from_values(arr, value1, value2):
    idx1 = index_of(arr, value1, -1)
    idx2 = index_of(arr, value2, idx1)
    return sorted([idx1 + 1, idx2 + 1])


def solve(arr, money):
    sorted_arr = sorted(arr)

    for i in range(len(sorted_arr)):
        complement = money - sorted_arr[i]
        location = binarysearch(sorted_arr, i, complement)
        if location:
            print(*get_idx_from_values(arr, sorted_arr[i], complement))
            break


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        money = int(input().strip())
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        solve(arr, money)
