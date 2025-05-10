import sys
input = sys.stdin.readline

import math

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def find(x):
    if x == uf[x]:
        return x
    
    root_node = find(uf[x])
    uf[x] = root_node

    return root_node

def union(a, b):
    A, B = find(a), find(b)

    uf[B] = A

n, m = map(int, input().split())

points = [[0, 0]]

edge_cnt = 0

for _ in range(n):
    points.append(list(map(int, input().split())))

uf = list(range(n + 1))

for _ in range(m):
    a, b = map(int, input().split())

    if find(a) != find(b):
        union(a, b)
        edge_cnt += 1

mst = 0

edges = []

for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        edges.append((i, j, dist(points[i], points[j])))

edges.sort(key = lambda x : x[2])

for edge in edges:
    a, b, cost = edge

    if find(a) != find(b):
        union(a, b)
        mst += cost
        edge_cnt += 1

    if edge_cnt == n - 1:
        break

print(f"{mst:.2f}")