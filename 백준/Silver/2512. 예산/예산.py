import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

max_budget = int(input())

left, right = 0, max(arr)

optim = 0
optim_budget = -1

while left <= right:
    mid = (left + right) // 2

    budget = sum(min(mid, city) for city in arr)

    if budget <= max_budget:
        optim = mid
        optim_budget = budget
        left = mid + 1
    else:
        right = mid - 1

print(optim)
