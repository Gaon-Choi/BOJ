import heapq
import math
import sys
input = sys.stdin.readline

def dijkstra(src):
    pq = []

    dist = [math.inf] * (n + 1)
    visited = [False] * (n + 1)

    dist[src] = 0
    heapq.heappush(pq, (0, src))

    while len(pq) > 0:
        curr_dist, u = heapq.heappop(pq)

        if visited[u]:
            continue
        visited[u] = True

        for v, cost in graph[u]:
            new_dist = curr_dist + cost

            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist

n, m = map(int, input().split())

start_node = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    src, tgt, w = map(int, input().split())
    graph[src].append([tgt, w])

dist_arr = dijkstra(start_node)

for i in range(1, n + 1):
    print(dist_arr[i] if dist_arr[i] < math.inf else "INF")