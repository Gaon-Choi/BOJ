import sys
input = sys.stdin.readline

S, C = map(int, input().split())

arr = []

for _ in range(S):
    arr.append(int(input()))

left, right = 1, max(arr)

max_length = 0

while left <= right:
    mid = (left + right) // 2

    total_cnt = sum(pa // mid for pa in arr)

    if total_cnt >= C:
        left = mid + 1
        max_length = max(max_length, mid)
    else:
        right = mid - 1

total_length = sum(arr)
used_length = C * max_length

print(total_length - used_length)