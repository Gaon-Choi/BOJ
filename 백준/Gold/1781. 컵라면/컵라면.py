import sys
input = sys.stdin.readline

import heapq

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().split())))

arr.sort()

pq = []

for i in range(n):
    heapq.heappush(pq, arr[i][1])

    # 현 시점보다 더 많은 개수를 선택했다면 가장 라면 수 작은거 하나 빼기
    if len(pq) > arr[i][0]:
        heapq.heappop(pq)

total_answer = 0

while pq:
    total_answer += heapq.heappop(pq)

print(total_answer)