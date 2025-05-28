import sys
input = sys.stdin.readline

from collections import defaultdict

ddict = defaultdict(int)

n = int(input())

for _ in range(n):
    ddict[input().strip()] += 1

arr = list(ddict.items())

arr.sort(key = lambda x : (-x[1], x[0]))

print(arr[0][0])
