import sys
input = sys.stdin.readline

# find operation
def find(n):
    if uf[n] == n:
        return n
        
    root_node = find(uf[n])
    
    uf[n] = root_node
    
    return root_node

# union operation
def union(a, b):
    A = find(a)
    B = find(b)
    
    uf[A] = B

n = int(input())

points = []

for i in range(1, n + 1):
    x, y, z = map(int, input().split())
    points.append((i, x, y, z))

edges = []

for dim in range(1, 4):
    points.sort(key = lambda point : point[dim])

    for i in range(n - 1):
        edges.append((abs(points[i][dim] - points[i + 1][dim]), points[i][0], points[i + 1][0]))

edges.sort()

mst = 0
e = 0
uf = list(range(n + 1))

for edge in edges:
    w, u, v = edge

    if find(u) != find(v):
        mst += w
        union(u, v)
        e += 1

    if e == n - 1:
        break

print(mst)