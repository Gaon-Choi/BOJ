from collections import deque

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs():
    q = deque(tomatoes)

    for tomato in tomatoes:
        x, y = tomato
        visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if is_reachable(nx, ny) and visited[nx][ny] == -1 and matrix[nx][ny] != -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])


m, n = map(int, input().split())

tomatoes = []
matrix = []

for row in range(n):
    arr = list(map(int, input().split()))

    for col in range(len(arr)):
        if arr[col] == 1:
            tomatoes.append([row, col])

    matrix.append(arr)

visited = [[-1] * m for _ in range(n)]

bfs()

max_time = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            if visited[i][j] == -1:
                print(-1)
                exit(0)
            
            max_time = max(max_time, visited[i][j])

print(max_time)