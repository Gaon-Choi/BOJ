import sys
input = sys.stdin.readline

def find(x):
    if x == uf[x]:
        return x
    
    root_node = find(uf[x])
    uf[x] = root_node

    return root_node

def union(x, y):
    X, Y = find(x), find(y)
    uf[Y] = X

while True:
    V, E = map(int, input().split())

    if V == E == 0:
        break

    uf = list(range(V + 1))

    edges = []
    total_cost = 0

    for _ in range(E):
        start, end, cost = map(int, input().split())
        
        edges.append((start, end, cost))

    edges.sort(key = lambda x : x[2])

    for edge in edges:
        start, end, cost = edge

        if find(start) != find(end):
            union(start, end)
        else:
            total_cost += cost

    print(total_cost)
