import sys
input = sys.stdin.readline

import heapq

T = int(input())

for _ in range(T):
    N = int(input())

    min_pq = []
    max_pq = []

    size = 0
    global_idx = 0

    deleted = set()

    for _ in range(N):
        mode, elem = input().split()
        elem = int(elem)

        if mode == "I":
            heapq.heappush(min_pq, (elem, global_idx))
            heapq.heappush(max_pq, (-elem, global_idx))
            global_idx += 1
            size += 1

        else:
            # 최댓값 삭제
            if elem == 1:
                while max_pq:
                    elem, idx = heapq.heappop(max_pq)

                    if idx not in deleted:
                        deleted.add(idx)
                        size -= 1
                        break
            else:
                while min_pq:
                    elem, idx = heapq.heappop(min_pq)

                    if idx not in deleted:
                        deleted.add(idx)
                        size -= 1
                        break

    while min_pq:
        elem, idx = min_pq[0]

        if idx not in deleted:
            break

        heapq.heappop(min_pq)

    while max_pq:
        elem, idx = max_pq[0]

        if idx not in deleted:
            break

        heapq.heappop(max_pq)

    if size == 0:
        print('EMPTY')
    else:
        print(-max_pq[0][0], min_pq[0][0])