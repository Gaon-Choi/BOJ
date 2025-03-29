import sys
input = sys.stdin.readline

def bfs(v):
    cnt = 0

    cnt += 1
    visited[v] = cnt

    queue = [v]

    while queue:
        x = queue.pop(0)

        for adj in sorted(graph[x]):
            if not visited[adj]:
                cnt += 1
                visited[adj] = cnt
                queue.append(adj)
    

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(r)

print(*visited[1:], sep="\n")