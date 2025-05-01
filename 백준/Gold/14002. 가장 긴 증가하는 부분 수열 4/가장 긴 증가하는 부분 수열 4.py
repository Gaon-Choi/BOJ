import sys
input = sys.stdin.readline

n = int(input())

dp = [1] * n
prev = [-1] * n

arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            if dp[i] < dp[j] + 1:
                prev[i] = j
                dp[i] = dp[j] + 1

loc = -1
max_length = 0

for i in range(n):
    if max_length < dp[i]:
        max_length = dp[i]
        loc = i

print(max_length)

res = []

while loc != -1:
    res.append(arr[loc])
    loc = prev[loc]

res.reverse()

print(*res)