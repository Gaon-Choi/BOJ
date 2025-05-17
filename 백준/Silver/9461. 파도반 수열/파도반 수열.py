import sys
input = sys.stdin.readline

n = int(int(input()))

queries = []

for _ in range(n):
    queries.append(int(input()))

max_ = max(queries)

dp = [0] * (max_ + 1)
dp[1] = 1; dp[2] = 1; dp[3] = 1

for i in range(4, max_ + 1):
    dp[i] = dp[i - 2] + dp[i - 3]

for q in queries:
    print(dp[q])