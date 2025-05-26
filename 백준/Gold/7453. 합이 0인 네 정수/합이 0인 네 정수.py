import sys
input = sys.stdin.readline

from collections import Counter

ab = Counter()

n = int(input())

A, B, C, D = [], [], [], []

cnt = 0

for _ in range(n):
    a, b, c, d = map(int, input().split())
    
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for elem1 in A:
    for elem2 in B:
        ab[elem1 + elem2] += 1

for elem1 in C:
    for elem2 in D:
        target = -(elem1 + elem2)
        cnt += ab[target]

print(cnt)