strings = sorted([input() for _ in range(int(input()))])
for _ in range(int(input())):
    query = input()
    count = 0
    for strs in strings:
        if query == strs:
            count += 1
    print(count)

from collections import Counter

d = Counter([input().strip() for _ in range(int(input()))])
print(*[d[input().strip()] for _ in range(int(input()))], sep='\n')