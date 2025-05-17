def lower_bound(arr, k):
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < k:
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

    return len(dp), lis_result

def restore_lis(arr, lis_result):
    lis_length = max(lis_result)

    result = []

    prev = float('inf')

    # 뒤에서부터 추적적
    for i in reversed(range(len(arr))):
        if lis_result[i] == lis_length and arr[i] < prev:
            result.append(arr[i])
            prev = arr[i]
            lis_length -= 1

    # 역순으로 정렬하여 리턴
    return result[-1::-1]

n = int(input())

arr = list(map(int, input().split()))

lis_len, lis_res = lcs(arr)

print(lis_len)

result = restore_lis(arr, lis_res)

print(*result)
