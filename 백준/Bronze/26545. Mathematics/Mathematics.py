import sys
input = sys.stdin.readline

n = int(input())
ans = 0

for _ in range(n):
    ans += int(input())

print(ans)