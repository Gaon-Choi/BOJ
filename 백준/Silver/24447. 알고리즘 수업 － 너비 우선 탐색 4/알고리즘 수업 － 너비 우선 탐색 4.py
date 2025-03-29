import sys
input = sys.stdin.readline

def bfs(v):
    cnt = 1
    visited[v] = 0
    cnt_arr[v] = cnt
    cnt += 1

    queue = [v]

    while queue:
        x = queue.pop(0)

        for adj in sorted(graph[x], reverse = True):
            if visited[adj] == -1:
                visited[adj] = visited[x] + 1
                cnt_arr[adj] = cnt
                cnt += 1
                
                queue.append(adj)
    
n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [-1] * (n + 1)
cnt_arr = [0] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(r)

total = 0

for i in range(1, n + 1):
    total += cnt_arr[i] * visited[i]

print(total)