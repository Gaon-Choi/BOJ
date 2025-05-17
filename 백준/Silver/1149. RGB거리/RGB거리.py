import sys
input = sys.stdin.readline

n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().split())))

dp = [[0] * 3 for _ in range(n)]

dp[0] = matrix[0][:]

# 0 R, 1 G, 2 B

R, G, B = 0, 1, 2

for i in range(1, n):
    dp[i][R] = min(dp[i - 1][G], dp[i - 1][B]) + matrix[i][R]
    dp[i][G] = min(dp[i - 1][R], dp[i - 1][B]) + matrix[i][G]
    dp[i][B] = min(dp[i - 1][R], dp[i - 1][G]) + matrix[i][B]

print(min(dp[n - 1]))