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


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)
