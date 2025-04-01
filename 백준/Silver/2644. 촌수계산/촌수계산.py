from collections import deque

import sys
input = sys.stdin.readline

def bfs(x):
    queue = deque([x])
    visited[x] = 0

    while queue:
        x = queue.popleft()

        for adj in graph[x]:
            if visited[adj] == -1:
                visited[adj] = visited[x] + 1
                queue.append(adj)

n = int(input())

a, b = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(a)

print(visited[b])