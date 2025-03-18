import sys
input = sys.stdin.readline

sys.setrecursionlimit(1000000)

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

V, E = 10000, 100000

v, e = map(int, input().split())

uf = list(range(V + 1))

edges = []

for _ in range(e):
    # (A, B, C) : A와 B를 잇는 간선 (가중치 = C)
    edges.append(list(map(int, input().split())))
    
edges.sort(key = lambda x:x[2])

mst = 0

for e in edges:
    A, B, w = e[0], e[1], e[2]
    
    if find(A) != find(B):
        union(A, B)
        mst += w
    
print(mst)