def qsort(ar, start, end):
    if end - start <= 0:
        return ar
    pivot = ar[end]
    ind = start
    for i in range(start, end):
        if ar[i] <= pivot:
            ar[i], ar[ind] = ar[ind], ar[i]
            ind += 1
    ar[ind],ar[end] = ar[end], ar[ind]
    print(' '.join(str(x) for x in ar))
    # left side
    ar = qsort(ar, start, ind - 1)
    # right side
    ar = qsort(ar, ind + 1, end)
    return ar


n = int(input())
ar = [int(x) for x in input().split()]
qsort(ar, 0, n - 1)
