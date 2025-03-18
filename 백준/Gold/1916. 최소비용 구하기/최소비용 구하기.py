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

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    src, tgt, w = map(int, input().split())
    graph[src].append([tgt, w])

start_node, end_node = map(int, input().split())
    
dist_arr = dijkstra(start_node)

print(dist_arr[end_node])