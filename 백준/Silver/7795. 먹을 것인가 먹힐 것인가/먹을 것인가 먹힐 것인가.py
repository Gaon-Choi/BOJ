import sys
input = sys.stdin.readline

def upper_bound(arr, k):
    left, right = 0, len(arr) - 1

    mid_idx = len(arr)

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] > k:
            right = mid - 1
            mid_idx = min(mid_idx, mid)
        else:
            left = mid + 1

    return mid_idx

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    arr1.sort()

    total = 0

    for i in range(b):
        lidx = upper_bound(arr1, arr2[i])

        total += (a - lidx)

    print(total)