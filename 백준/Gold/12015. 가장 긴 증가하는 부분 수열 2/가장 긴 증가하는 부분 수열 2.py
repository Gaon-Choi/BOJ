import sys
input = sys.stdin.readline

def lower_bound(arr, target):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left

def lcs(arr):
    dp = []

    lis_result = [0] * len(arr)

    for i, num in enumerate(arr):
        bis_idx = lower_bound(dp, num)

        if bis_idx == len(dp):
            dp.append(num)
        else:
            dp[bis_idx] = num

        lis_result[i] = bis_idx + 1

    return lis_result

n = int(input())

arr = list(map(int, input().split()))

dp = [1] * n

res = lcs(arr)

print(max(res))