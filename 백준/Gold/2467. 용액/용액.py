import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left, right = 0, n - 1

res = float('inf')

answer = []

while left < right:
    sum_ = arr[left] + arr[right]

    if abs(sum_) <= res:
        res = abs(sum_)
        answer = [arr[left], arr[right]]

    if sum_ < 0:
        left += 1
    else:
        right -= 1

print(*answer)
