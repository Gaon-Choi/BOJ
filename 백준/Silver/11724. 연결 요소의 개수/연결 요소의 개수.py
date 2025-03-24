import sys
input = sys.stdin.readline

from collections import deque

def is_reachable(x):
    return 0 < x <= n

def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = True

    while queue:
        x_ = queue.popleft()

        for v in graph[x_]:
            if is_reachable(v) and not visited[v]:
                visited[v] = True
                queue.append(v)

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)

cnt = 0

for v in range(1, n + 1):
    if not visited[v]:
        bfs(v)
        cnt += 1

print(cnt)