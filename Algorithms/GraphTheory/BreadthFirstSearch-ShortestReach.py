#!/bin/python3

import sys

class Graph:
    def __init__(self, n):
        self.edges = {i: set() for i in range(n)}
        self.dist = {i: -1 for i in range(n)}

    def connect(self, i, j):
        self.edges[i] = self.edges[i].union({j})
        self.edges[j] = self.edges[j].union({i})

    def find_all_distances(self, s):
        queue = [s]
        self.dist[s] = 0
        for node in queue:
            neigh = [j for j in self.edges[node] if j not in queue]
            for i in neigh: self.dist[i] = self.dist[node] + 6
            queue.extend(neigh)
        print(*[self.dist[i] for i in range(n) if i != s])


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        graph = Graph(n)
        for edges_i in range(m):
           edges_t = [int(edges_temp) for edges_temp in input().strip().split(' ')]
           graph.connect(edges_t[0]-1, edges_t[1] - 1)
        s = int(input().strip())
        graph.find_all_distances(s - 1)
