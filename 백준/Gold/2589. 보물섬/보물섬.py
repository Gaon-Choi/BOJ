import sys
input = sys.stdin.readline

from collections import deque

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < m and (matrix[x][y] != "W")

def bfs(x, y):
    visited = [[-1] * m for _ in range(n)]

    visited[x][y] = 0
    queue = deque([[x, y]])

    cnt = 0

    while queue:
        x_, y_ = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x_ + dx, y_ + dy

            if is_reachable(nx, ny) and visited[nx][ny] == -1:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x_][y_] + 1
                cnt = max(cnt, visited[nx][ny])

    return cnt


n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

max_dist = -1

for x in range(n):
    for y in range(m):
        if matrix[x][y] != "W":
            cnt = bfs(x, y)
            max_dist = max(max_dist, cnt)

print(max_dist)