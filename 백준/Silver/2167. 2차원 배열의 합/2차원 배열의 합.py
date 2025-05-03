import sys
input = sys.stdin.readline

n, m = map(int, input().split())

mat = []

for _ in range(n):
    mat.append(list(map(int, input().split())))

dp = [[0] * (m + 1) for _ in range(n + 1)]

for x in range(1, n + 1):
    dp[x][1] = dp[x - 1][1] + mat[x - 1][0]

for y in range(1, m + 1):
    dp[1][y] = dp[1][y - 1] + mat[0][y - 1]

for x in range(2, n + 1):
    for y in range(2, m + 1):
        dp[x][y] = dp[x - 1][y] + dp[x][y - 1] - dp[x - 1][y - 1] + mat[x - 1][y - 1]

t = int(input())

for _ in range(t):
    x0, y0, x1, y1 = map(int, input().split())
    print(dp[x1][y1] - dp[x1][y0 - 1] - dp[x0 - 1][y1] + dp[x0 - 1][y0 - 1])