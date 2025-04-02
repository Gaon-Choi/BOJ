from collections import deque

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < m and not visited[x][y]

def bfs(x, y):
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    queue = deque([[x, y]])
    visited[x][y] = True

    cnt = 0

    while queue:
        x, y = queue.popleft()
        cnt += 1

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if is_reachable(nx, ny) and matrix[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append([nx, ny])
    
    return cnt

n, m = map(int, input().split())

matrix = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    matrix.append(list(map(int, input().split())))

paintings = []

for i in range(n):
    for j in range(m):
        if not visited[i][j] and matrix[i][j] == 1:
            paintings.append(bfs(i, j))

print(len(paintings))

if paintings:
    print(max(paintings))
else:
    print(0)