import heapq

import sys
input = sys.stdin.readline

pq = []

n = int(input())

for _ in range(n):
    heapq.heappush(pq, int(input()))

cost = 0

while len(pq) >= 2:
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)

    cost += (a + b)

    heapq.heappush(pq, a + b)

print(cost)