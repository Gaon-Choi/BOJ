from collections import deque

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(arr):
    temp_cnt = 0

    pq = deque(arr)

    for x, y in arr:
        visited[x][y] = True

    while pq:
        x, y = pq.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if is_reachable(nx, ny) and matrix[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                matrix[nx][ny] = 2
                pq.append([nx, ny])

    safe_count = sum(row.count(0) for row in matrix)
    return safe_count
                

n, m = map(int, input().split())

matrix_ = []
for _ in range(n):
    matrix_.append(list(map(int, input().split())))

empty_loc = []

for i in range(n):
    for j in range(m):
        if matrix_[i][j] == 0:
            empty_loc.append([i, j])

max_cnt = 0

for i in range(len(empty_loc)):
    for j in range(i + 1, len(empty_loc)):
        for k in range(j + 1, len(empty_loc)):
            matrix = [x[:] for x in matrix_]

            x1, y1 = empty_loc[i]
            x2, y2 = empty_loc[j]
            x3, y3 = empty_loc[k]

            matrix[x1][y1] = 1; matrix[x2][y2] = 1; matrix[x3][y3] = 1

            visited = [[False] * m for _ in range(n)]

            temp_arr = []

            for x in range(n):
                for y in range(m):
                    if matrix[x][y] == 2:
                        temp_arr.append([x, y])

            max_cnt = max(max_cnt, bfs(temp_arr))


print(max_cnt)