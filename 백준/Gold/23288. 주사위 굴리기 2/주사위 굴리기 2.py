from collections import deque

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < m

def get_bfs_score():
    global x, y

    val = matrix[x][y]

    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True

    queue = deque([[x, y]])

    cnt = 0

    while queue:
        x_, y_ = queue.popleft()
        cnt += 1

        for dx, dy in zip(dxs, dys):
            nx, ny = x_ + dx, y_ + dy
            if is_reachable(nx, ny) and (not visited[nx][ny]) and matrix[nx][ny] == val:
                visited[nx][ny] = True
                queue.append([nx, ny])

    return cnt * val

def rotate_dice():
    global curr
    u, f, r = dice

    if curr == 0:
        return [7 - r, f, u]
    elif curr == 1:
        return [7 - f, u, r]
    elif curr == 2:
        return [r, f, 7 - u]
    else:
        return [f, 7 - u, r]

n, m, k = map(int, input().split())

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
curr = 0    # 현재 방향

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

dice = [1, 5, 3]
total_score = 0
x, y = 0, 0

for _ in range(k):
    if not is_reachable(x + dxs[curr], y + dys[curr]):
        curr = abs(curr + 2) % 4

    x += dxs[curr % 4]
    y += dys[curr % 4]
    
    total_score += get_bfs_score()

    dice = rotate_dice()

    value = 7 - dice[0] # 바닥면 숫자

    # 바닥면 숫자가 해당칸보다 작으면 반시계 회전
    if value < matrix[x][y]:
        curr = abs(curr - 1 + 4) % 4
    # 바닥면 숫자가 해당칸보다 크면 시계 회전
    elif value > matrix[x][y]:
        curr = abs(curr + 1) % 4

print(total_score)