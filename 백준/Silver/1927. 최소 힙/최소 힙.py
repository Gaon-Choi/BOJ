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
            result.append(deleted)
        else:
            result.append(0)
    else:
        heapq.heappush(heap, elem)
        size += 1
        
for elem in result:
    print(elem)