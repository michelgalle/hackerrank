#!/bin/python3

import sys
import bisect
import heapq


def is_odd(n):
    return n & 1 == 1


class MinHeap:
    """
    Maintain a max-heap for the lower half of values
    and a min-heap for higher half of values
    """

    def __init__(self):
        self.heap = []

    def peek(self):
        return self.heap[0] if self.heap else float('+inf')

    def push(self, data):
        heapq.heappush(self.heap, data)

    def replace(self, data):
        return heapq.heapreplace(self.heap, data)

    def size(self):
        return len(self.heap)


class MaxHeap(MinHeap):
    """
    Pythons heapq methods are for a min-heap,
    so data are inverted in the max heap
    """

    def peek(self):
        return -self.heap[0] if self.heap else float('-inf')

    def push(self, data):
        heapq.heappush(self.heap, -data)

    def replace(self, data):
        return -heapq.heapreplace(self.heap, -data)


class RunningMedian:
    def __init__(self):
        self._minheap = MinHeap()
        self._maxheap = MaxHeap()

    def __str__(self):
        return "\n".join([" ".join(map(str, map(lambda d: -d, self._maxheap.heap))),
                          " ".join(map(str, self._minheap.heap))])

    def add(self, data):
        if self._maxheap.size() == self._minheap.size():
            if data < self._minheap.peek() or not len(self._minheap.heap):
                self._maxheap.push(data)
            else:
                self._maxheap.push(self._minheap.replace(data))
        else:
            if data > self._maxheap.peek() or not len(self._maxheap.heap):
                self._minheap.push(data)
            else:
                self._minheap.push(self._maxheap.replace(data))

    def median(self):
        if self._maxheap.size() == self._minheap.size():
            return (self._maxheap.peek() + self._minheap.peek()) / 2
        else:
            return self._maxheap.peek()


rm = RunningMedian()
for _ in range(int(input())):
    a = int(input())
    rm.add(a)
    print("{:.1f}".format(rm.median()))

'''    
n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    bisect.insort(a,a_t)
    if is_odd(a_i+1):
        print("{:.1f}".format(a[(a_i+1)//2]))
    else:
        print("{:.1f}".format((a[a_i//2] + a[(a_i+1)//2]) / 2))
'''