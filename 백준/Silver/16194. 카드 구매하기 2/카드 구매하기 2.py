import sys
input = sys.stdin.readline

N = int(input())

INF = float('inf')

dp = [INF] * (N + 1)
dp[0] = 0

arr = list(map(int, input().split()))

for num_, elem in enumerate(arr):
    num = num_ + 1

    for i in range(num, N + 1):
        dp[i] = min(dp[i], dp[i - num] + elem)

print(dp[N])
