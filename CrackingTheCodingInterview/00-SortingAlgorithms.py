import bisect

'''
The algorithm works by comparing each item in the list with the item next to it,
and swapping them if required. In other words, the largest element has bubbled to the top of the array.
The algorithm repeats this process until it makes a pass all the way through the list without swapping any items.
'''
def bubble_sort(seq):
    changed = True
    while changed:
        changed = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
    return None

'''
Start with a sorted list of 1 element on the left, and N-1 unsorted items on the right. Take the first unsorted item 
(element #2) and insert it into the sorted list, moving elements as necessary. We now have a sorted list of size 2, and
 N -2 unsorted elements. Repeat for all elements.
'''
def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (l[j] > key) and (j >= 0):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key


def insertion_sort_bin(seq):
    for i in range(1, len(seq)):
        key = seq[i]
        # invariant: ``seq[:i]`` is sorted
        # find the least `low' such that ``seq[low]`` is not less then `key'.
        #   Binary search in sorted sequence ``seq[low:up]``:
        low, up = 0, i
        while up > low:
            middle = (low + up) // 2
            if seq[middle] < key:
                low = middle + 1
            else:
                up = middle
        # insert key at position ``low``
        seq[:] = seq[:low] + [key] + seq[low:i] + seq[i + 1:]


def insertion_sort_bin(seq):
    for i in range(1, len(seq)):
        bisect.insort(seq, seq.pop(i), 0, i)

'''
The algorithm works by selecting the smallest unsorted item and then swapping it with the item in the next position to
be filled. The selection sort works as follows: you look through the entire array for the smallest element, once you
find it you swap it (the smallest element) with the first element of the array. Then you look for the smallest element
 in the remaining array (an array without the first element) and swap it with the second element. Then you look for the
smallest element in the remaining array (an array without first and second elements) and swap it with the third element,
and so on.
'''
def selection_sort(lst):
    for i, e in enumerate(lst):
        mn = min(range(i,len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e
    return lst


'''
Merge sort takes advantage of the ease of merging already sorted lists into a new sorted list. The basic idea is to 
split the collection into smaller groups by halving it until the groups only have one element or no elements (which are
both entirely sorted groups). Then merge the groups back together so that their elements are in order. This is how the
algorithm gets its “divide and conquer” description.

It is notable for having a worst case and average complexity of O(n*log(n)), and a best case complexity of O(n)
(for pre-sorted input).
'''
from heapq import merge


def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


'''
Heapsort is an in-place sorting algorithm with worst case and average complexity of   O(n logn).
The basic idea is to turn the array into a binary heap structure, which has the property that it allows efficient retrieval and removal of the maximal element.
We repeatedly "remove" the maximal element from the heap, thus building the sorted list from back to front.
Heapsort requires random access, so can only be used on an array-like data structure.
'''
def swap(i, j):
    list[i], list[j] = list[j], list[i]


def heapify(end, i):
    l = 2 * i + 1
    r = 2 * (i + 1)
    max = i
    if l < end and list[i] < list[l]:
        max = l
    if r < end and list[max] < list[r]:
        max = r
    if max != i:
        swap(i, max)
        heapify(end, max)


def heap_sort():
    end = len(list)
    start = end // 2 - 1
    for i in range(start, -1, -1):
        heapify(end, i)
    for i in range(end - 1, 0, -1):
        swap(i, 0)


'''
 Approach:
 radix sort, like counting sort and bucket sort, is an integer based
 algorithm (i.e. the values of the input array are assumed to be
 integers). Hence radix sort is among the fastest sorting algorithms
 around, in theory. The particular distinction for radix sort is
 that it creates a bucket for each cipher (i.e. digit); as such,
 similar to bucket sort, each bucket in radix sort must be a
 growable list that may admit different keys.
 For decimal values, the number of buckets is 10, as the decimal
 system has 10 numerals/cyphers (i.e. 0,1,2,3,4,5,6,7,8,9). Then
 the keys are continuously sorted by significant digits.
=====================================================================
'''
def radixsort(aList):
    RADIX = 10
    tmp, placement = -1, 1

    while True:
        # declare and initialize buckets
        buckets = [list() for _ in range(RADIX)]

        # split aList between lists
        for i in aList:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)

        print(buckets)
        # empty lists into aList array
        if len(buckets[0]) == len(aList):
            return buckets[0]
        aList = []
        for b in range(RADIX):
            aList += buckets[b]

        # move to next digit
        placement *= RADIX
