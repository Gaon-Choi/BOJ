import sys
input = sys.stdin.readline

def find(x):
    while x != uf[x]:
        uf[x] = uf[uf[x]]  # 경로 압축
        x = uf[x]
    return x

    return root_node

def union(x, y):
    X, Y = find(x), find(y)

    if X != Y:
        uf[Y] = X

n, m = map(int, input().split())

uf = list(range(n + 1))

num = 1

flag = False

for _ in range(m):
    a, b = map(int, input().split())

    if find(a) != find(b):
        union(a, b)
    else:
        flag = True
        break

    num += 1

    if num > m:
        num = 1

print(num if flag else 0)
