import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    min_diff = float('inf')
    hash_ = dict()

    left, right = 0, n - 1

    while left < right:
        sum_ = arr[left] + arr[right]

        diff = abs(sum_ - k)

        if diff not in hash_:
            hash_[diff] = 1
        else:
            hash_[diff] += 1

        if min_diff > diff:
            min_diff = diff

        if sum_ >= k:
            right -= 1
        else:
            left += 1
    
    print(hash_[min_diff])

