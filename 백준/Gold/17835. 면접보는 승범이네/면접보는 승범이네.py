import sys
input = sys.stdin.readline

import heapq

def dijkstra():
    global result

    pq = []

    for target in interview_place:
        heapq.heappush(pq, (0, target))
        result[target] = 0

    while pq:
        dist, city = heapq.heappop(pq)

        if result[city] < dist:
            continue

        for nx_city, nx_cost in graph[city]:
            new_dist = dist + nx_cost
            if new_dist < result[nx_city]:
                result[nx_city] = new_dist
                heapq.heappush(pq, (new_dist, nx_city))

INF = float('inf')

N, M, K = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    src, tgt, cost = map(int, input().split())
    #graph[src].append((tgt, cost))
    graph[tgt].append((src, cost))

interview_place = list(map(int, input().split()))

result = [INF] * (N + 1)

dijkstra()

max_city, max_cost = -1, -1

for idx, cost in enumerate(result):
    if cost != INF and cost > max_cost:
        max_city = idx
        max_cost = cost

print(max_city)
print(max_cost)