import heapq
import sys

N = int(sys.stdin.readline())

heap = []
result = []
size = 0

for _ in range(N):
    elem = int(sys.stdin.readline())
    if elem == 0:
        if size > 0:
            deleted = heapq.heappop(heap)
            size -= 1
            result.append(deleted[0] * deleted[1])
        else:
            result.append(0)
    else:
        heapq.heappush(heap, [abs(elem), -1 if elem < 0 else 1])
        size += 1
        
for elem in result:
    print(elem)