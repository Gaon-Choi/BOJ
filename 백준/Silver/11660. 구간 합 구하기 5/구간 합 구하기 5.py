import sys
input = sys.stdin.readline

N, M = map(int, input().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

smatrix = [[0] * (N + 1) for _ in range(N + 1)]

for x in range(1, N + 1):
    for y in range(1, N + 1):
        smatrix[x][y] = smatrix[x - 1][y] + smatrix[x][y - 1] - smatrix[x - 1][y - 1] + matrix[x - 1][y - 1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    print(smatrix[x2][y2] - smatrix[x2][y1 - 1] - smatrix[x1 - 1][y2] + smatrix[x1 - 1][y1 - 1])
