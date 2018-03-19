#!/bin/python3

import sys
'''
def insertionSort(arr):
    count = 0
    for i in range(1, len(arr)):
        key = arr[i]
        # invariant: ``seq[:i]`` is sorted
        # find the least `low' such that ``seq[low]`` is not less then `key'.
        #   Binary search in sorted sequence ``seq[low:up]``:
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if arr[middle] <= key:
                low = middle + 1
            elif arr[middle] > key:
                up = middle
        # insert key at position ``low``
        count += i-low
        arr[:] = arr[:low] + [key] + arr[low:i] + arr[i + 1:]
    return count


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = insertionSort(arr)
        print(result)'''


def count_inv(arr, len_arr):
    if len_arr <= 1: return 0

    m = len_arr >> 1
    arr_l, arr_r = arr[:m], arr[m:]
    len_arr_l, len_arr_r = m, len_arr - m
    s = count_inv(arr_l, len_arr_l) + count_inv(arr_r, len_arr_r)

    lp = rp = p = 0
    while lp < len_arr_l and rp < len_arr_r:
        if arr_l[lp] <= arr_r[rp]:
            arr[p] = arr_l[lp]
            lp += 1
        else:
            arr[p] = arr_r[rp]
            s += len_arr_l - lp
            rp += 1
        p += 1

    while lp < len_arr_l:
        arr[p] = arr_l[lp]
        lp += 1
        p += 1

    while rp < len_arr_r:
        arr[p] = arr_r[rp]
        rp += 1
        p += 1

    return s

T = int(input())
for t in range(T):
    N = int(input())
    arr = [int(i) for i in input().split()]
    print(count_inv(arr, N))