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

edges = []

for _ in range(m):
    start, end, cost = map(int, input().split())
    edges.append((start, end, cost))

edges.sort(key = lambda x: x[2])

mst = 0
last_cost = 0

for edge in edges:
    start, end, cost = edge

    if find(start) != find(end):
        union(start, end)
        mst += cost
        last_cost = cost

print(mst - last_cost)