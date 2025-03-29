from collections import deque

def dfs(x):
    cnt = 1
    stack = deque([x])

    while stack:
        p = stack.pop()

        if not visited[p]:
            visited[p] = cnt
            cnt += 1
        else:
            continue

        for adj in sorted(graph[p], reverse=True):
            if visited[adj] == 0:
                stack.append(adj)

n, m, r = map(int, input().split())

visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(r)

print(*visited[1:], sep = "\n")