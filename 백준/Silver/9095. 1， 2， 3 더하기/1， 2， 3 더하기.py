n = int(input())

max_num = 0

arr = []

for _ in range(n):
    temp = int(input())
    arr.append(temp)
    max_num = max(max_num, temp)

dp = [0] * (max_num + 1)
dp[0] = 1

for i in range(1, max_num + 1):
    if i - 1 >= 0:
        dp[i] += dp[i - 1]
    if i - 2 >= 0:
        dp[i] += dp[i - 2]
    if i - 3 >= 0:
        dp[i] += dp[i - 3]

for elem in arr:
    print(dp[elem])