import sys
input = sys.stdin.readline

def find(x):
    while x != uf[x]:
        uf[x] = uf[uf[x]]
        x = uf[x]

    return x

def union(x, y):
    X, Y = find(x), find(y)

    if X != Y:
        uf[Y] = X

T = int(input())

for t in range(1, T + 1):
    n = int(input())
    uf = list(range(n + 1))

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        union(a, b)

    print("Scenario {t}:".format(t=t))

    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        
        if find(a) != find(b):
            print(0)
        else:
            print(1)

    print()