import sys
input = sys.stdin.readline

import heapq
import math

T = int(input())

for _ in range(T):
    left, right = [], []

    n = int(input())

    arr = []

    for _ in range(math.ceil(n / 10)):
        arr.extend(list(map(int, input().split())))

    res = []

    for idx, elem in enumerate(arr):
        heapq.heappush(left, -elem)

        if right and -left[0] > right[0]:
            left_max = -heapq.heappop(left)
            right_min = heapq.heappop(right)

            heapq.heappush(left, -right_min)
            heapq.heappush(right, left_max)

        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))

        if idx % 2 == 0:
            res.append(-left[0])

    print(len(res))

    for idx, val in enumerate(res):
        if (idx != 0) and (idx % 10 == 0):
            print()

        print(val, end=" ")

    print()