import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

for i in range(n):
    for j in range(m):
        print(matrix[i][m - j - 1], end = "")
    print()
