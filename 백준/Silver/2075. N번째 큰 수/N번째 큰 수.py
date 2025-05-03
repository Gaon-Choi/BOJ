import sys
input = sys.stdin.readline

import heapq

pq = []

n = int(input())

for _ in range(n):
    arr = list(map(int, input().split()))

    for elem in arr:
        heapq.heappush(pq, elem)
        if len(pq) > n:
            heapq.heappop(pq)

pq.sort(reverse = True)

print(pq[n - 1])