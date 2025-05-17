import sys
input = sys.stdin.readline

N, K = map(int, input().split())

dp = [[0] * (N + 1) for _ in range(K + 1)]

for i in range(1, K + 1):
    importance, cost_time = map(int, input().split())

    for j in range(1, N + 1):
        if j < cost_time:
            dp[i][j] = dp[i - 1][j]

        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost_time] + importance)
    
print(dp[K][N])
