from collections import deque

def bfs(root):
    visited = [False] * (n + 1)
    q = deque()
    q.append(root)
    visited[root] = True

    while q:
        v = q.popleft()

        for adj in graph[v]:
            if not visited[adj]:
                visited[adj] = True
                parent[adj] = v
                q.append(adj)

n = int(input())

graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for _ in range(n - 1):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

root = 1

bfs(root)

print(*parent[root + 1:], sep="\n")