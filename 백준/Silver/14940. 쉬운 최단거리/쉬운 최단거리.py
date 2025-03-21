n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

visited = [[-1] * m for _ in range(n)]

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def find_destination():
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                return [i, j]

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < m and visited[x][y] == -1

def bfs(x_, y_):
    queue = [[x_, y_]]
    visited[x_][y_] = 0

    while len(queue) > 0:
        x, y = queue.pop(0)

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if is_reachable(nx, ny) and matrix[nx][ny] != 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])

dest_x, dest_y = find_destination()

bfs(dest_x, dest_y)

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            visited[i][j] = 0

for i in range(n):
    for j in range(m):
        print(visited[i][j], end=" ")
    print()