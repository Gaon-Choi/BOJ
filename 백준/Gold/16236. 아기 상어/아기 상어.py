from collections import deque

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(si, sj):
    visited = [[-1] * n for _ in range(n)]
    visited[si][sj] = 0

    q = deque([[si, sj]])

    fish = []

    while q:
        x, y = q.popleft()
        
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if is_reachable(nx, ny) and (matrix[nx][ny] <= SHARK) and (visited[nx][ny] == -1):
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])

                if 0 < matrix[nx][ny] < SHARK:
                    fish.append([visited[nx][ny], nx, ny])

    fish.sort()

    return fish[0] if fish else None


n = int(input())
SHARK = 2

matrix = []
curr_x, curr_y = 0, 0

for i in range(n):
    arr = list(map(int, input().split()))

    for j in range(len(arr)):
        if arr[j] == 9:
            curr_x, curr_y = i, j

    matrix.append(arr)

total_time = 0

eat_num = 0

while True:
    fish = bfs(curr_x, curr_y)

    if fish:
        d, fish_x, fish_y= fish

        total_time += d

        eat_num += 1

        if eat_num == SHARK:
            SHARK += 1
            eat_num = 0

        matrix[curr_x][curr_y] = 0
        matrix[fish_x][fish_y] = 0

        curr_x, curr_y = fish_x, fish_y

        matrix[curr_x][curr_y] = 9
    else:
        break

print(total_time)