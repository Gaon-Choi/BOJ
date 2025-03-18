import math
import sys
input = sys.stdin.readline

sys.setrecursionlimit(1000000)

size = 100

def find(n):
    if uf[n] == n:
        return n
        
    root_node = find(uf[n])
    
    uf[n] = root_node
    
    return root_node
    
def union(a, b):
    A = find(a)
    B = find(b)
    
    uf[A] = B

n = int(input())
stars = []
idx = 0

uf = list(range(size + 1))

edges = []

for _ in range(n):
    stars.append(list(map(float, input().split())))
    
for i in range(len(stars)):
    for j in range(i + 1, len(stars)):
        edges.append([i + 1, j + 1, math.sqrt((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2)])
    
edges.sort(key = lambda x:x[2])

mst = 0

for e in edges:
    A, B, w = e[0], e[1], e[2]
    
    if find(A) != find(B):
        union(A, B)
        mst += w
    
print(mst)