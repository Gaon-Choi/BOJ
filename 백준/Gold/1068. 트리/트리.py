import sys
sys.setrecursionlimit(50000)

def dfs(node):
    global leaf_count

    if node == delete_node:
        return
    
    child_exists = False

    for child in tree[node]:
        if child != delete_node:
            dfs(child)
            child_exists = True

    if not child_exists:
        leaf_count += 1

n = int(input())

tree = [[] for _ in range(n)]
parents = list(map(int, input().split()))
root = -1

delete_node = int(input())

for child, parent in enumerate(parents):
    if parent == -1:
        root = child

    else:
        tree[parent].append(child)

leaf_count = 0

dfs(root)

print(leaf_count)