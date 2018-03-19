def bubble_sort(seq):
    changed = True
    swaps = 0
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
                swaps += 1
    return swaps


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swaps = bubble_sort(a)
print("Array is sorted in {0} swaps.".format(swaps))
print("First Element: {0}".format(a[0]))
print("Last Element: {0}".format(a[-1]))