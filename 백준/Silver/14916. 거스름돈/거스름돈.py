import sys
input = sys.stdin.readline

n = int(input())

dp = [-1] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    a, b = -1, -1

    if i - 2 >= 0 and dp[i - 2] != -1:
        a = dp[i - 2]

    if i - 5 >= 0 and dp[i - 5] != -1:
        b = dp[i - 5]

    if a == b == -1:
        dp[i] = -1
    elif a == -1 and b != -1:
        dp[i] = b + 1
    elif a != -1 and b == -1:
        dp[i] = a + 1
    else:
        dp[i] = min(a, b) + 1

print(dp[n])
    