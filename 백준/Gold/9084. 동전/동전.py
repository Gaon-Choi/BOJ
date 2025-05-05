import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    dp = [0] * 10001
    dp[0] = 1

    arr = list(map(int, input().split()))
    total = int(input())

    for i in range(n):
        coin = arr[i]
        
        for j in range(coin, total + 1):
            dp[j] += dp[j - coin]

    print(dp[total])