import math
import sys
input = sys.stdin.readline

def floyd_warshall(graph):
    size = len(graph)

    dist = [[math.inf] * size for _ in range(size)]
    prev = [[-1] * size for _ in range(size)]

    for i in range(size):
        dist[i][i] = 0

    for u in range(size):
        for v, cost in graph[u]:
            if dist[u][v] > cost:
                dist[u][v] = cost
                prev[u][v] = u

    for k in range(1, size):
        for i in range(1, size):
            for j in range(1, size):
                if (dist[i][j] > dist[i][k] + dist[k][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
                    prev[i][j] = prev[k][j]

    return dist, prev

def reconstruct_path(u, v, prev):
    if prev[u][v] == -1:
        return []
    
    path = []
    while v != u:
        path.append(v)
        v = prev[u][v]
    path.append(u)
    path.reverse()

    return path

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    src, tgt, cost = map(int, input().split())
    graph[src].append((tgt, cost))

dist, prev = floyd_warshall(graph)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] < math.inf:
            print(dist[i][j], end=" ")
        else:
            print(0, end=" ")
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        path = reconstruct_path(i, j, prev)
        print(len(path), *path)