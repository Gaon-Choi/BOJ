import sys
input = sys.stdin.readline

import heapq

n = int(input())

arr = []

for _ in range(n):
    p, d = map(int, input().split())
    arr.append((d, p))

arr.sort()

pq = []

for i in range(n):
    heapq.heappush(pq, arr[i][1])

    if len(pq) > arr[i][0]:
        heapq.heappop(pq)

total = 0

while pq:
    total += heapq.heappop(pq)

print(total)