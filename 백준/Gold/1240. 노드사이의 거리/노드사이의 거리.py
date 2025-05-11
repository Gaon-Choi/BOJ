import sys
input = sys.stdin.readline

from collections import deque

def bfs(start, end):
    visited = [False] * (n + 1)
    dist = [0] * (n + 1)

    visited[start] = True
    queue = deque([start])

    while queue:
        x = queue.popleft()

        if x == end:
            return dist[x]
            break

        for adj, cost in graph[x]:
            if not visited[adj]:
                visited[adj] = True
                dist[adj] = dist[x] + cost
                queue.append(adj)

    return 0


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    start, end, cost = map(int, input().split())

    graph[start].append((end, cost))
    graph[end].append((start, cost))

for _ in range(m):
    start, end = map(int, input().split())
    print(bfs(start, end))