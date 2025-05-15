import sys
input = sys.stdin.readline

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)
        self.size = size

    def update(self, idx, diff):
        while idx <= self.size:
            self.tree[idx] += diff
            idx += idx & -idx

    def query(self, idx):
        result = 0

        while idx > 0:
            result += self.tree[idx]
            idx -= idx & -idx

        return result
    
    def range_query(self, start, end):
        return self.query(end) - self.query(start - 1)
    
n, m, k = map(int, input().split())

fenwick_tree = FenwickTree(n)

for idx in range(1, n + 1):
    fenwick_tree.update(idx, int(input()))

for _ in range(m + k):
    a, b, c = map(int, input().split())

    if a == 1:
        fenwick_tree.update(b, c - (fenwick_tree.query(b) - fenwick_tree.query(b - 1)))
    else:
        print(fenwick_tree.range_query(b, c))