import sys
input = sys.stdin.readline

from collections import deque

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x_, y_):
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]

    queue = deque([[x_, y_]])
    visited[x_][y_] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if is_reachable(nx, ny) and (not visited[nx][ny]) and matrix[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append([nx, ny])


t = int(input())
result = []

for _ in range(t):
    m, n, k = map(int, input().split())

    matrix = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        matrix[x][y] = 1

    res = 0

    for x in range(n):
        for y in range(m):
            if matrix[x][y] == 1 and not visited[x][y]:
                bfs(x, y)
                res += 1

    result.append(res)

for res in result:
    print(res)