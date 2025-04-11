def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < n

munji = [
    [
        [0,0,2,0,0],
        [0,10,7,1,0],
        [5,0,0,0,0],
        [0,10,7,1,0],
        [0,0,2,0,0]
    ],
    [
        [0,0,0,0,0],
        [0,1,0,1,0],
        [2,7,0,7,2],
        [0,10,0,10,0],
        [0,0,5,0,0]
    ],
    [
        [0,0,2,0,0],
        [0,1,7,10,0],
        [0,0,0,0,5],
        [0,1,7,10,0],
        [0,0,2,0,0]
    ],
    [
        [0,0,5,0,0],
        [0,10,0,10,0],
        [2,7,0,7,2],
        [0,1,0,1,0],
        [0,0,0,0,0]
    ],
]

def add_dust(x, y, dust):
    global ans

    if not is_reachable(x, y):
        ans += dust
    else:
        matrix[x][y] += dust

def move():
    global x, y

    if x == 0 and y == -1:
        return

    added_dust = 0

    for i in range(5):
        for j in range(5):
            dust = matrix[x][y] * munji[d][i][j] // 100
            add_dust(x + i - 2, y + j - 2, dust)
            added_dust += dust

    add_dust(x + dxs[d], y + dys[d], matrix[x][y] - added_dust)


dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

x, y = n // 2, n // 2

num = 1
d = 0
flag = 0

ans = 0

while True:
    for _ in range(num):
        x += dxs[d]
        y += dys[d]
        
        if x == 0 and y == -1:
            print(ans)
            exit(0)

        move()

    flag += 1
    d = (d + 1) % 4

    if flag == 2:
        flag = 0
        num += 1

print(ans)