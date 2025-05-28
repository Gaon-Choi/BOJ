import sys
input = sys.stdin.readline

from collections import defaultdict

ddict = defaultdict(int)

n, m = map(int, input().split())

for _ in range(n):
    ddict[input().strip()] += 1

arr = list(filter(lambda x: len(x[0]) >= m, list(ddict.items())))

arr.sort(key = lambda x: (-x[1], -len(x[0]), x[0]))

for k, v in arr:
    print(k)
