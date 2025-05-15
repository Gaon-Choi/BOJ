import sys
input = sys.stdin.readline

import heapq

n = int(input())

left = []   # max-heap
right = []  # min-heap

for _ in range(n):
    elem = int(input())

    heapq.heappush(left, -elem)

    if right and -left[0] > right[0]:
        left_max = -heapq.heappop(left)
        right_min = heapq.heappop(right)

        heapq.heappush(left, -right_min)
        heapq.heappush(right, left_max)

    if len(left) > len(right) + 1:
        heapq.heappush(right, -heapq.heappop(left))

    print(-left[0])