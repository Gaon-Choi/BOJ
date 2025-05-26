import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

total = float('inf')

for i in range(n - 1):
    total = min(total, (arr[i] + arr[i + 1]) * x)

print(total)