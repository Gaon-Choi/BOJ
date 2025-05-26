import sys
input = sys.stdin.readline

h, w = map(int, input().split())

matrix = []

for _ in range(h):
    matrix.append(list(input().strip()))

for x in range(h):
    for y in range(w):
        if matrix[x][y] != ".":
            matrix[x][w - y - 1] = matrix[x][y]

for row in matrix:
    print("".join(row))
