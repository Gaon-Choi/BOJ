import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    for i in range(1, n + 1):
        dp[0][i] = i

    for floor in range(1, k + 1):
        for room in range(1, n + 1):
            dp[floor][room] = dp[floor][room - 1] + dp[floor - 1][room]

    print(dp[k][n])
