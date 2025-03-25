import sys
input = sys.stdin.readline

def find(uf, x):
    if uf[x] == x:
        return x
    
    root_node = find(uf, uf[x])
    uf[x] = root_node

    return root_node

def union(uf, size, x, y):
    X, Y = uf[x], uf[y]

    uf[Y] = X
    size[X] += size[Y]

t = int(input())

for _ in range(t):
    idx = 1
    friends = dict()

    n = int(input())

    uf = list(range(2*n + 1))
    size = [1] * (2 * n + 1)

    for _ in range(n):
        a, b = input().split()

        if a not in friends:
            friends[a] = idx
            idx += 1
        
        if b not in friends:
            friends[b] = idx
            idx += 1

        A, B = friends[a], friends[b]

        if find(uf, A) != find(uf, B):
            union(uf, size, A, B)

        print(size[find(uf, A)])
    