import heapq
import math

def dijkstra(src):
    dist = [math.inf] * (n + 1)
    prev_path = [-1] * (n + 1)

    pq = []

    dist[src] = 0
    heapq.heappush(pq, (0, src))

    while pq:
        curr_dist, u = heapq.heappop(pq)

        for v, cost in sorted(graph[u]):
            new_dist = curr_dist + cost

            if new_dist < dist[v]:
                dist[v] = new_dist
                prev_path[v] = u
                heapq.heappush(pq, (new_dist, v))

    return dist, prev_path

def get_path(prev_arr, target):
    path = []

    while target != -1:
        path.append(target)
        target = prev_arr[target]
    
    path = path[-1::-1]
    return path

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

source, target = map(int, input().split())

dist_result, path_result = dijkstra(source)

optimal_path = get_path(path_result, target)

print(dist_result[target])

print(len(optimal_path))

print(*optimal_path)