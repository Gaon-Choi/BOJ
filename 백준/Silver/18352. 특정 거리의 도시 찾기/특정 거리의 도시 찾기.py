import heapq

def dijkstra(src):
    dist = [1e10] * (N + 1)

    dist[src] = 0
    pq = []
    heapq.heappush(pq, (0, src))

    while pq:
        cost, v = heapq.heappop(pq)

        for adj in graph[v]:
            new_dist = cost + 1

            if new_dist < dist[adj]:
                dist[adj] = new_dist
                heapq.heappush(pq, (new_dist, adj))

    return dist
    

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

dist_result = dijkstra(X)

temp = []

for i in range(1, N + 1):
    if dist_result[i] == K:
        temp.append(i)

temp.sort()

if temp:
    print(*temp, sep="\n")
else:
    print(-1)