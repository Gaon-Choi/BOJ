from collections import deque

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(visited, x_, y_):
    queue = deque([[x_, y_]])
    visited[x_][y_] = True

    loc_list = []
    total_cost = 0

    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    while queue:
        x, y = queue.popleft()

        loc_list.append([x, y])
        total_cost += matrix[x][y]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if is_reachable(nx, ny) and (not visited[nx][ny]) and (l <= abs(matrix[nx][ny] - matrix[x][y]) <= r):
                visited[nx][ny] = True
                queue.append([nx, ny])

    return loc_list, total_cost

def balance_egg_group(llist, tcost):
    avg = tcost // len(llist)

    for x, y in llist:
        matrix[x][y] = avg

def average_eggs():
    visited = [[False] * n for _ in range(n)]

    flag = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                llist, tcost = bfs(visited, i, j)

                if len(llist) != 1:
                    balance_egg_group(llist, tcost)
                    flag = True

    return flag

n, l, r = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

cnt = 0

while True:
    res = average_eggs()

    if not res:
        break

    cnt += 1

print(cnt)