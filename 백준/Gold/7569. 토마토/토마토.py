from collections import deque

directions = [
    (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)
]

def is_reachable(x, y, z):
    return 0 <= x < N and 0 <= y < M and 0 <= z < H

def bfs(arr):
    global N, M, H

    q = deque(arr)

    max_day = 0

    for k, i, j in arr:
        visited[k][i][j] = 0

    while q:
        h, x, y = q.popleft()
        max_day = max(max_day, visited[h][x][y])

        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, h + dz

            if is_reachable(nx, ny, nz) and visited[nz][nx][ny] == -1 and matrix[nz][nx][ny] == 0:
                visited[nz][nx][ny] = visited[h][x][y] + 1
                q.append([nz, nx, ny])

    return max_day

def find_non_ripe_fruit():
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if matrix[h][i][j] == 0 and visited[h][i][j] == -1:
                    return -1

    return result


M, N, H = map(int, input().split())

matrix = []
apples = []

for k in range(H):
    temp = []
    for i in range(N):
        temp_arr = list(map(int, input().split()))
        for j in range(len(temp_arr)):
            if temp_arr[j] == 1:
                apples.append([k, i, j])
        temp.append(temp_arr)
    matrix.append(temp)

visited = [[[-1] * M for _ in range(N)] for _ in range(H)]

result = bfs(apples)

print(find_non_ripe_fruit())