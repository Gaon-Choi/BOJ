import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

matrix = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)
    matrix[b].append(a)
    
def bfs(n_):
    global cnt
    visited[n_] = True
    queue = [n_]
    
    while len(queue) > 0:
        n = queue.pop(0)
        for adj in matrix[n]:
            if not visited[adj]:
                cnt += 1
                visited[adj] = True
                queue.append(adj)
                
cnt = 0

bfs(1)

print(cnt)