dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def is_reachable(x, y):
    return 0 <= x < m and 0 <= y < n and matrix[x][y] != 1 and not visited[x][y]

def dfs(x, y):
    stack = []

    stack.append([x, y])
    visited[x][y] = True

    cnt = 1

    while stack:
        x_, y_ = stack.pop()

        for dx, dy in zip(dxs, dys):
            nx, ny = x_ + dx, y_ + dy

            if is_reachable(nx, ny):
                cnt += 1
                visited[nx][ny] = True
                stack.append([nx, ny])

    return cnt


m, n, k = map(int, input().split())

matrix = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]

for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())

    for y in range(sx, ex):
        for x in range(sy, ey):
            matrix[x][y] = 1

result = []

for x in range(m):
    for y in range(n):
        if not visited[x][y] and matrix[x][y] != 1:
            cnt = dfs(x, y)
            result.append(cnt)

result.sort()

print(len(result))
for res in result:
    print(res, end = " ")