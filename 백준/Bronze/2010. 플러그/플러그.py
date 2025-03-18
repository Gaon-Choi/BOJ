import sys

n = int(input())

total = 0

for _ in range(n):
    total += int(sys.stdin.readline())
    
print(total - (n - 1))