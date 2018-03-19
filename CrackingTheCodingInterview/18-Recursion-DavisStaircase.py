memory = {1:1, 2:2, 3:4}
def num_ways(n):
    if not n in memory.keys():
        memory[n] = num_ways(n-1) + num_ways(n-2) + num_ways(n-3)
    return memory[n]


s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    print(num_ways(n))