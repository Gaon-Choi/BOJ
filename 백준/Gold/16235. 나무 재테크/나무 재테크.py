dxs = [0, 0, 1, 1, 1, -1, -1, -1]
dys = [1, -1, 1, -1, 0, 1, -1, 0]

def is_reachable(x, y):
    return 0 <= x < n and 0 <= y < n

def get_all_virus():
    total_virus = 0

    for i in range(n):
        for j in range(n):
            if virus[i][j]:
                total_virus += len(virus[i][j])

    return total_virus

def eat_yangbun_and_die(x, y):
    global virus, dead_virus
    
    new_virus = []

    for v in sorted(virus[x][y]):
        if matrix[x][y] - v >= 0:
            matrix[x][y] -= v
            new_virus.append(v + 1)
        else:
            dead_virus[x][y].append(v)

    virus[x][y] = new_virus

def die_and_add_yangbun(x, y):
    global matrix, dead_virus

    for v in dead_virus[x][y]:
        matrix[x][y] += (v // 2)

    dead_virus[x][y] = []

def spread_virus(x, y):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if is_reachable(nx, ny):
            virus[nx][ny].append(1)

def add_yangbun():
    for i in range(n):
        for j in range(n):
            matrix[i][j] += add_matrix[i][j]

n, m, k = map(int, input().split())

virus = [[[] for _ in range(n)] for _ in range(n)]
dead_virus = [[[] for _ in range(n)] for _ in range(n)]

add_matrix = []
matrix = [[5] * n for _ in range(n)]

for _ in range(n):
    add_matrix.append(list(map(int, input().split())))

for _ in range(m):
    r, c, age = map(int, input().split())
    r -= 1; c -= 1
    virus[r][c].append(age)

for _ in range(k):
    for i in range(n):
        for j in range(n):
            eat_yangbun_and_die(i, j)

    for i in range(n):
        for j in range(n):
            die_and_add_yangbun(i, j)

    for i in range(n):
        for j in range(n):
            for v in virus[i][j]:
                if v % 5 == 0:
                    spread_virus(i, j)

    add_yangbun()

print(get_all_virus())