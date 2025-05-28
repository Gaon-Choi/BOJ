import sys
input = sys.stdin.readline

from collections import deque

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x0, y0):
    visited[x0][y0] = True
    q = deque([(x0, y0)])

    cnt = 0

    while q:
        x, y = q.popleft()
        cnt += 1

        for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
            nx, ny = x + dx, y + dy
            if is_reachable(nx, ny) and matrix[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

    return cnt

n, m, k = map(int, input().split())

matrix = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

max_area = 0

for _ in range(k):
    x, y = map(int, input().split())
    matrix[x - 1][y - 1] = 1

for x in range(n):
    for y in range(m):
        if matrix[x][y] == 1 and not visited[x][y]:
            max_area = max(max_area, bfs(x, y))

print(max_area)
