def find(x):
    if x == uf[x]:
        return x
    
    root_node = find(uf[x])
    uf[x] = root_node

    return root_node

def union(x, y):
    X, Y = find(x), find(y)
    uf[Y] = X


n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

edges = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            edges.append((i + 1, j + 1, matrix[i][j]))

uf = list(range(n + 1))

edges.sort(key = lambda x: x[2])

mst = 0

for edge in edges:
    start, end, cost = edge

    if find(start) != find(end):
        union(start, end)
        mst += cost

print(mst)