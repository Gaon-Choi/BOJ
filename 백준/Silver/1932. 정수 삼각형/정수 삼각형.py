import sys
input = sys.stdin.readline

n = int(input())

trimat = []

for _ in range(n):
    trimat.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(n)]

dp[0][0] = trimat[0][0]

for i in range(1, n):
    # i층 -> i + 1개

    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + trimat[i][j]
        elif j == i:
            dp[i][j] = dp[i - 1][j - 1] + trimat[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + trimat[i][j]

print(max(dp[n - 1]))
