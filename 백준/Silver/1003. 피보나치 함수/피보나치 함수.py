import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [[1, 0], [0, 1]]

for i in range(2, max(arr) + 1):
    dp.append([dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]])
    
for elem in arr:
    print(dp[elem][0], dp[elem][1])