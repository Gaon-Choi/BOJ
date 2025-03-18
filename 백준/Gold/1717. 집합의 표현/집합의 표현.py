import sys
input = sys.stdin.readline

sys.setrecursionlimit(100000)

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
    
def is_equal(a, b):
    return find(a) == find(b)

n, m = map(int, input().split())

uf = list(range(n + 1))

result = []

for _ in range(m):
    op, a, b = map(int, input().split())
    
    # find
    if op == 1:
        result.append(is_equal(a, b))
    # union
    elif op == 0:
        union(a, b)
        
for res in result:
    print("YES" if res else "NO")