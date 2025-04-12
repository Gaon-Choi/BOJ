from collections import deque

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(x_, y_):
    visited[x_][y_][0] = True
    q = deque()
    q.append((x_, y_, 0, 1))

    while q:
        x, y, is_brick_break, depth = q.popleft()

        if x == n - 1 and y == m - 1:
            return depth

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if not is_reachable(nx, ny):
                continue

            if matrix[nx][ny] == 1 and is_brick_break == 0 and not visited[nx][ny][1]:
                visited[nx][ny][1] = True
                q.append((nx, ny, is_brick_break + 1, depth + 1))
            elif matrix[nx][ny] == 0 and not visited[nx][ny][is_brick_break]:
                visited[nx][ny][is_brick_break] = True
                q.append((nx, ny, is_brick_break, depth + 1))

    return -1


n, m = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, list(input()))))

visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]

print(bfs(0, 0))
