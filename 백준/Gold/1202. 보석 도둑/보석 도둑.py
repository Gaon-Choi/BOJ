import sys
input = sys.stdin.readline

import heapq

n, k = map(int, input().split())

jewels = []

for _ in range(n):
    jewels.append(list(map(int, input().split())))

bags = []

for _ in range(k):
    bags.append(int(input()))

jewels.sort()
bags.sort()

jewel_loc = 0

pq = []

total_value = 0

for i in range(k):
    while (jewel_loc < n and jewels[jewel_loc][0] <= bags[i]):
        heapq.heappush(pq, -jewels[jewel_loc][1])
        jewel_loc += 1

    if pq:
        elem = -heapq.heappop(pq)
        total_value += elem
        
print(total_value)