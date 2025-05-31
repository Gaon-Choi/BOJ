import sys
input = sys.stdin.readline

A, B = input().strip().split()

size_a, size_b = len(A), len(B)

cost = 1e9

for i in range(size_b - size_a + 1):
    temp = 0

    for j in range(size_a):
        if A[j] != B[i + j]:
            temp += 1

    cost = min(cost, temp)
    
print(cost)
