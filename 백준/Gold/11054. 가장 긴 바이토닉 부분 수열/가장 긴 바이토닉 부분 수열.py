import sys
input = sys.stdin.readline

def lcs(arr):
    size = len(arr)

    dp = [1] * size

    for i in range(size):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp

n = int(input())

arr = list(map(int, input().split()))

lcs_result = lcs(arr)
lds_result = lcs(arr[::-1])[::-1]

res = -1

for c, d in zip(lcs_result, lds_result):
    res = max(res, c + d - 1)

print(res)