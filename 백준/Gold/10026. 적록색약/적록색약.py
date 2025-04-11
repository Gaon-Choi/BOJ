from collections import deque

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < n

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def bfs(visited, x_, y_, isBlind = False):
    visited[x_][y_] = True

    q = deque([[x_, y_]])

    color = matrix[x_][y_]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if is_reachable(nx, ny) and not visited[nx][ny] and ((matrix[nx][ny] == color) \
            or (isBlind and (color in ["R", "G"]) and (matrix[nx][ny] in ["R", "G"]))):
                visited[nx][ny] = True
                q.append([nx, ny])


n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

cnt1 = 0
cnt2 = 0

for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            bfs(visited1, i, j, isBlind=False)
            cnt1 += 1
        
        if not visited2[i][j]:
            bfs(visited2, i, j, isBlind=True)
            cnt2 += 1

print(cnt1, cnt2)