import sys
input = sys.stdin.readline

def bfs(v):
    visited[v] = 0

    queue = [v]

    while queue:
        x = queue.pop(0)

        for adj in sorted(graph[x], reverse = True):
            if visited[adj] == -1:
                visited[adj] = visited[x] + 1
                queue.append(adj)
    
n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(r)

print(*visited[1:], sep="\n")