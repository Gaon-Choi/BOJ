import sys
input = sys.stdin.readline

from collections import deque

def is_reachable(x, y, z):
    return 0 <= x < l and 0 <= y < r and 0 <= z < c

def bfs(x0, y0, z0):
    visited[x0][y0][z0] = 0
    q = deque([(x0, y0, z0)])

    while q:
        x, y, z = q.popleft()

        if (x, y, z) == end:
            return visited[x][y][z]

        for dx, dy, dz in zip([1, 0, -1, 0, 0, 0], [0, 1, 0, -1, 0, 0], [0, 0, 0, 0, 1, -1]):
            nx, ny, nz = x + dx, y + dy, z + dz

            if is_reachable(nx, ny, nz) and (matrix[nx][ny][nz] != "#") and (visited[nx][ny][nz] == -1):
                visited[nx][ny][nz] = visited[x][y][z] + 1
                q.append((nx, ny, nz))

    return -1

while True:
    l, r, c = map(int, input().split())

    visited = [[[-1] * c for _ in range(r)] for _ in range(l)]

    start, end = None, None

    if l == r == c == 0:
        break

    matrix = []

    for x in range(l):
        floor = []

        for y in range(r):
            temp = list(input().strip())
            
            for z in range(c):
                if temp[z] == "S":
                    start = (x, y, z)
                elif temp[z] == "E":
                    end = (x, y, z)

            floor.append(temp)

        matrix.append(floor)

        a = input().strip()

    res = bfs(*start)

    if res == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {res} minute(s).")

