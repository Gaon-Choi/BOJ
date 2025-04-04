import math
import heapq

def dijkstra(graph, source):
    dist = [math.inf] * (n + 1)

    pq = []

    dist[source] = 0
    heapq.heappush(pq, (0, source))

    while pq:
        src_cost, src_vertex = heapq.heappop(pq)

        for u, cost in graph[src_vertex]:
            new_dist = src_cost + cost

            if new_dist < dist[u]:
                dist[u] = new_dist
                heapq.heappush(pq, (new_dist, u))

    return dist

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
rev_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())

    graph[start].append((end, cost))
    rev_graph[end].append((start, cost))

# 파티장 갈 때
rev_graph_result = dijkstra(rev_graph, x)
# 집으로 돌아갈 때
graph_result = dijkstra(graph, x)

max_dist = -1

for i in range(1, n + 1):
    new_dist = rev_graph_result[i] + graph_result[i]
    if max_dist < new_dist:
        max_dist = new_dist

print(max_dist)