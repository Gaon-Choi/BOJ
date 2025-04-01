from collections import deque

import sys
input = sys.stdin.readline

def make_zero(h):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] <= h:
                matrix[i][j] = 0

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < n and matrix[x][y] != 0

def bfs(x, y):
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    queue = deque([[x, y]])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if is_reachable(nx, ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])

n = int(input())

max_height = 0
matrix = []
for _ in range(n):
    arr = list(map(int, input().split()))
    max_height = max(max_height, max(arr))
    matrix.append(arr)

max_cnt = 0

for h in range(max_height + 1):
    visited = [[False] * n for _ in range(n)]
    make_zero(h)

    cnt = 0
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0 and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    max_cnt = max(cnt, max_cnt)

print(max_cnt)