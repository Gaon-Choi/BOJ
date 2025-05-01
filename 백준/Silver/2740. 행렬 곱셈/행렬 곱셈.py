import sys
input = sys.stdin.readline

mat1 = []
mat2 = []

n, m = map(int, input().split())

for _ in range(n):
    mat1.append(list(map(int, input().split())))

m, k = map(int, input().split())

for _ in range(m):
    mat2.append(list(map(int, input().split())))

result = [[0] * k for _ in range(n)]

for x in range(n):
    for y in range(k):
        for z in range(m):
            result[x][y] += mat1[x][z] * mat2[z][y]

for res in result:
    print(*res)