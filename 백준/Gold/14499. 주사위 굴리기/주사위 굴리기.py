def rotate_dice(curr):
    global dice

    up, front, right, bottom, back, left = dice

    if curr == 1:   # 동
        dice = [left, front, up, right, back, bottom]
    elif curr == 2: # 서
        dice = [right, front, bottom, left, back, up]
    elif curr == 3: # 남
        dice = [back, up, right, front, bottom, left]
    else:   # 북
        dice = [front, bottom, right, back, up, left]

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < m

n, m, x, y, k = map(int, input().split())

dxs = [0, 0, 0, -1, 1]
dys = [0, 1, -1, 0, 0]

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

# 1 동, 2 서, 3 남, 4 북
moves = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]

for i in range(k):
    d = moves[i]

    nx, ny = x + dxs[d], y + dys[d]

    if not is_reachable(nx, ny):
        continue

    x, y = nx, ny

    rotate_dice(d)

    if matrix[x][y] == 0:
        matrix[x][y] = dice[3]
    elif matrix[x][y] != 0:
        dice[3] = matrix[x][y]
        matrix[x][y] = 0

    print(dice[0])