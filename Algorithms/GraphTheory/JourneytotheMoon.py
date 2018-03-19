#!/bin/python3

import sys


class Graph:
    def __init__(self, n, astronaut):
        self.astronauts = {i: set([i]) for i in range(n)}
        self.keys = [i for i in range(n)]
        for a,b in astronaut:
            key = self.keys[b]
            if a not in self.astronauts[key]:
                ast = self.astronauts[key]
                self.astronauts[self.keys[a]].update(ast)
                for i in ast:
                    self.keys[i] = self.keys[a]
                self.astronauts[key] = set()

    def countPermutations(self):
        sum = 0
        result = 0
        for i in self.astronauts:
            if len(self.astronauts[i])> 0:
                result += sum * len(self.astronauts[i])
                sum += len(self.astronauts[i])

        return result


def journeyToMoon(n, astronaut):
    astronauts = Graph(n, astronaut)
    return astronauts.countPermutations()


if __name__ == "__main__":
    n, p = input().strip().split(' ')
    n, p = [int(n), int(p)]
    astronaut = []
    for astronaut_i in range(p):
       astronaut_t = [int(astronaut_temp) for astronaut_temp in input().strip().split(' ')]
       astronaut.append(astronaut_t)
    result = journeyToMoon(n, astronaut)
    print(result)
