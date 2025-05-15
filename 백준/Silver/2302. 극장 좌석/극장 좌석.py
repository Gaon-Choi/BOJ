import sys
input = sys.stdin.readline

n = int(input())

dp = [1] * (n + 2)
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

vips = []

m = int(input())

for _ in range(m):
    vips.append(int(input()))

vips.sort()

prev = 0
ans = 1

for vip in vips:
    ans *= dp[vip - prev - 1]
    prev = vip

ans *= dp[n - prev]

print(ans)