import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort()

left, right = 0, 0

min_diff = float('inf')

while right < n:
    diff = arr[right] - arr[left]

    if diff < m:
        right += 1

    else:
        left += 1
        min_diff = min(min_diff, diff)

        if left > right:
            right = left

print(min_diff)
