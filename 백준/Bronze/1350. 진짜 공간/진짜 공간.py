import sys
input = sys.stdin.readline

import math

n = int(input())
arr = list(map(int, input().split()))
limit = int(input())

total = 0

for elem in arr:
    if elem == 0:
        continue

    total += math.ceil(elem / limit)

print(total * limit)
