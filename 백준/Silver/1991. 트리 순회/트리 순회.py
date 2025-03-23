import sys
input = sys.stdin.readline

def preorder(root):
    if root:
        left, right = tree[root]
    else:
        return []

    return [root] + preorder(left) + preorder(right)

def inorder(root):
    if root:
        left, right = tree[root]
    else:
        return []

    return inorder(left) + [root] + inorder(right)

def postorder(root):
    if root:
        left, right = tree[root]
    else:
        return []

    return postorder(left) + postorder(right) + [root]

n = int(input())

tree = dict()

for _ in range(n):
    node, left, right = input().split()

    if left == ".":
        left = None
    
    if right == ".":
        right = None

    tree[node] = (left, right)

print("".join(preorder("A")))
print("".join(inorder("A")))
print("".join(postorder("A")))