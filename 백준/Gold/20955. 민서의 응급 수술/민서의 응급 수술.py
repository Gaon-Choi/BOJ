import sys
input = sys.stdin.readline
sys.setrecursionlimit(50000)

def find(x):
    if x == uf[x]:
        return x
    
    root_node = find(uf[x])
    uf[x] = root_node

    return root_node

def union(x, y):
    X, Y = find(x), find(y)

    uf[Y] = X

n, m = map(int, input().split())

uf = list(range(n + 1))

cnt = 0

for _ in range(m):
    x, y = map(int, input().split())

    if find(x) != find(y):
        union(x, y)
    else:
        cnt += 1

for i in range(1, n + 1):
    if i == uf[i]:
        cnt += 1

# 루트 노드는 반드시 하나여야 하므로 1회 제외
cnt -= 1

print(cnt)