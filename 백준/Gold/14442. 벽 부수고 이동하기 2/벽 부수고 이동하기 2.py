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
        x, y, brick_count, depth = q.popleft()

        if x == n - 1 and y == m - 1:
            return depth

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if not is_reachable(nx, ny):
                continue

            if matrix[nx][ny] == 1 and brick_count < k and (not visited[nx][ny][brick_count + 1]):
                visited[nx][ny][brick_count + 1] = True
                q.append((nx, ny, brick_count + 1, depth + 1))
            elif matrix[nx][ny] == 0 and not visited[nx][ny][brick_count]:
                visited[nx][ny][brick_count] = True
                q.append((nx, ny, brick_count, depth + 1))

    return -1


n, m, k = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, list(input()))))

visited = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]

print(bfs(0, 0))